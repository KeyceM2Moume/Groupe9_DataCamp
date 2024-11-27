import streamlit as st
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch
import matplotlib.pyplot as plt

# Charger le tokenizer et le modèle
model_name = "cardiffnlp/xlm-roberta-base-tweet-sentiment-fr"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Fonction pour analyser les sentiments
def analyze_sentiments(df, comment_col, batch_size=16):
    predictions = []
    
    def batch_tokenize(texts):
        return tokenizer(texts, padding=True, truncation=True, return_tensors="pt", max_length=512)
    
    for i in range(0, len(df), batch_size):
        batch_reviews = df[comment_col][i:i+batch_size].tolist()
        if len(batch_reviews) == 0:
            continue
        inputs = batch_tokenize(batch_reviews)
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs.logits.detach().numpy()
        for logit in logits:
            sentiment = model.config.id2label[np.argmax(softmax(logit))]
            predictions.append(sentiment)
    return predictions

# Fonction pour générer des suggestions
def generate_recommendations(negative_reviews):
    suggestions = []
    for review in negative_reviews:
        review_lower = review.lower()
        if "bug" in review_lower or "erreur" in review_lower:
            suggestions.append("Corriger les bugs signalés.")
        elif "lent" in review_lower or "performance" in review_lower:
            suggestions.append("Optimiser les performances de l'application.")
        elif "crash" in review_lower or "planter" in review_lower:
            suggestions.append("Réduire les plantages et améliorer la stabilité.")
        elif "interface" in review_lower or "design" in review_lower:
            suggestions.append("Améliorer l'interface utilisateur pour plus de convivialité.")
        elif "fonctionnalité" in review_lower or "manque" in review_lower:
            suggestions.append("Ajouter ou améliorer les fonctionnalités demandées par les utilisateurs.")
        elif "audio" in review_lower or "qualité" in review_lower:
            suggestions.append("Améliorer la qualité audio pour une meilleure expérience.")
        else:
            suggestions.append("Examiner ce commentaire pour des retours spécifiques.")
    return suggestions

# Application Streamlit
st.title("Analyse des Sentiments des Avis Utilisateurs")
st.write("Cette application analyse les sentiments des avis et génère des insights basés sur les commentaires négatifs.")

# Charger le fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV contenant des avis", type=["csv"])
if uploaded_file is not None:
    # Charger les données
    df = pd.read_csv(uploaded_file, encoding='utf-8-sig', sep=';')
    st.write("Aperçu des données chargées :")
    st.write(df.head())

    # Permettre à l'utilisateur de définir les colonnes d'entrée
    st.subheader("Configuration des colonnes")
    columns = list(df.columns)
    comment_col = st.selectbox("Sélectionnez la colonne contenant les commentaires :", columns)
    date_col = st.selectbox("Sélectionnez la colonne contenant les dates (si disponible) :", columns)

    # Vérification de la colonne des commentaires
    if not comment_col:
        st.error("Veuillez sélectionner une colonne contenant les commentaires.")
    else:
        # Analyser les sentiments
        st.write("Analyse des sentiments en cours...")
        df['Sentiment'] = analyze_sentiments(df, comment_col)

        # Résumé des sentiments
        sentiment_counts = df['Sentiment'].value_counts()
        sentiment_percentage = sentiment_counts / len(df) * 100

        # Graphique en camembert des sentiments
        st.subheader("Répartition des Sentiments")
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # Graphique interactif : pourcentages de sentiments par colonnes sélectionnées
        st.subheader("Graphique interactif des pourcentages de sentiments")
        x_axis = st.selectbox("Sélectionnez une colonne pour l'axe X :", [col for col in columns if col != comment_col])

        if x_axis:
            percentages = df.groupby(x_axis)['Sentiment'].value_counts(normalize=True).unstack().fillna(0) * 100
            st.bar_chart(percentages)

        # Courbe d'évolution des sentiments
        st.subheader("Courbe d'évolution des sentiments")
        if date_col:
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
            df['Year'] = df[date_col].dt.year
            evolution = df.groupby('Year')['Sentiment'].value_counts(normalize=True).unstack().fillna(0) * 100
            fig, ax = plt.subplots()
            evolution.plot(kind="line", ax=ax)
            ax.set_title("Évolution des sentiments par année")
            ax.set_ylabel("Pourcentage")
            ax.set_xlabel("Année")
            st.pyplot(fig)
        else:
            st.write("Aucune colonne temporelle détectée pour générer la courbe d'évolution.")

        # Générer des recommandations basées sur les avis négatifs
        st.subheader("Suggestions d'amélioration")
        negative_reviews = df[df['Sentiment'] == 'negative'][comment_col].tolist()
        recommendations = generate_recommendations(negative_reviews)
        recommendation_df = pd.DataFrame({"Avis négatifs": negative_reviews, "Suggestions": recommendations})
        st.write(recommendation_df.head(10))  # Afficher les 10 premières recommandations

        # Télécharger les résultats
        st.subheader("Télécharger les résultats enrichis")
        csv = df.to_csv(index=False, encoding='utf-8-sig', sep=';')
        st.download_button("Télécharger les résultats", csv, "sentiments_results.csv", "text/csv")
