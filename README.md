# Groupe9_DataCamp
Spotify_Reviews
 
    1 - Guide d'installation et explication des demarches 

        A- Executer le code Web Scrapping (Scraping.ipynb)
    
 -!pip install google_play_scraper : Commande à effectuer dans le bash ou directement dans le notebook si pas déjà fait. 


        B-  Executer le notebook  (Cleaning.ipynb)

  -vérifier l'existence du fichier "Scrapped_reviews.csv" avant d'excuter le code. 
    
  -L'installation de python ou d'un framework si pas fais est nécessaire . Dans notre cas nous avons utilisés Anaconda. 
  
  -Le code prépare le dataset d'avis en le nettoyant, en filtrant les avis les plus pertinents et en formatant les données pour une analyse plus approfondie. Il utilise des techniques de nettoyage de texte et de manipulation de données pour obtenir un dataset de qualité. 
  
  -Si les bibliotheques Pandas et Re ne sont pas installé, il faudra le faire grâce aux commandes : pip install pandas et pip install re


        C-Exécution du code pour la Modelisation (FR_Modele_Roberta.ipynb) 

  - Vérifier l'existence de "top_1000_cleaned_reviews.csv" avant d'exécuter. 

  - Mise à jour pip(dans le bash)  pour éviter les problèmes de compatibilité : pip install --upgrade pip

  - Installation : La bibliothèque transformers(bash) est utilisée pour charger le modèle et le tokenizer : pip install transformers

  - Installation de PyTorch nécessaire pour les calculs du modèle, notamment pour les tenseurs et les prédictions(bash). : pip install torch

  - installation de scipy est utilisé pour la fonction softmax, qui transforme les logits en probabilités (bash). : pip install scipy

  - Certains modèles nécessitent un compilateur Rust pour traiter des composants comme les tokenizers. Si nécessaire, installez Rust(bash) : curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

  - La colone de prédictions sera ajouté au dataframe et le résultat sera sauvegardé dans un nouveau fichier csv.


        D- Dashboard avec Power BI
 
  - Ouverture : Téléchargez le fichier Dashboard.pbix et ouvrez-le avec Power BI Desktop.
  - Exploration : Naviguez entre les différents graphiques pour explorer les analyses spécifiques.
  - Si vous ne disposez pas de PowerBI vous pouvez ouvrir Dashboard.png pour consulter le dashboard 

        E- Creation de l'application streamlit (App.Py) 


  - Vérifier l'existence "reviews_with_sentiments.csv" avant d'esecuter le code
    
  -Installation de Streamlit (bash) : pip install streamlit 

  -Installation de Matplotlib (bash) : pip install matplotlib 

  -Le tokenizer décompose les textes en un format compréhensible par le modèle.

  -Traitement en lots : optimise la mémoire et le temps d'exécution.

  -Softmax : convertit les scores bruts du modèle en probabilités pour chaque classe.

  -Les sentiments (positif, négatif, neutre) sont déterminés par la classe ayant la probabilité maximale.

  - Le Code chargee le dataframe à analyser dans le dataframe et Créer l'interface utilisateur Streamlit, la creation des graphique et des recommandations.

  -Tester l'application en local grace à la commande (dans le terminal) : run App.by . Votre navigateur ouvrira l'application 

  

      2 - Accès à l'application 

  L'application est accessible à toutes personnes disposant du lien suivant :  https://groupe9datacamp-kpofbvqkesu68ba4wx7ltq.streamlit.app/


      3 - Comment utiliser l'application 

L'utilisation de l'application est très simple :

-Cliquer sur le lien de l'application 

-Dans la fenêtre "Drag and Drop files here" cliquer sur "Browse files" Pour selectionner un fichier csv à analyser (entrer "reviews_with_sentiments.csv") 

-Sélectionner la colonne contenant les commentaire, pour permettre aux graphiques dynamique de l'éviter car n'est pas pertinant pour les visualisations 

-Sélectionnez la colonne contenant les dates (at)(si disponible) nécessaire à la courbe d'évolution des sentiment en fonction des années 

-Cliquer sur télécharger les données pour sauvegarder les graphiques si besoin 
  



    

  

  

  
