# Groupe9_DataCamp
Spotify_Reviews

1 - Guide d'installation et explication des demarches 

    A- Web Scrapping 
    
 -!pip install google_play_scraper : Commande à effectuer dans le bash ou directement dans le notebook . 
est une commande utilisée en Python pour installer une bibliothèque appelée google-play-scraper. Cette bibliothèque offre un moyen programmatique d'interagir avec le Google Play Store, c'est-à-dire d'extraire des informations à partir de celui-ci.



    B-  Nettoyage du DataSet 
    
  -l'installation de python ou d'un framework si pas fais est necessaire . Dans notre cas nous avons utilisés anaconda qui est une distribution open-source de Python et R spécialement conçue pour les applications liées à la science des données, l'apprentissage automatique, l'analyse de données et le calcul scientifique.
  
  -Le code prépare le dataset d'avis en le nettoyant, en filtrant les avis les plus pertinents et en formatant les données pour une analyse plus approfondie. Il utilise des techniques de nettoyage de texte et de manipulation de données pour obtenir un dataset de qualité. Si les bibliotheques Pandas et Re ne sont pas installé faudra le faire grace à la commande : pip install pandas 


    C- Modelisation 
    
  -Récuperation du modèle Roberta dans hugging Face 

  - Mise à jour pip(dans le bash)  pour éviter les problèmes de compatibilité : pip install --upgrade pip

  - installation La bibliothèque transformers(bash) est utilisée pour charger le modèle et le tokenizer : pip install transformers

  - Installation de PyTorch nécessaire pour les calculs du modèle, notamment pour les tenseurs et les prédictions(bash). : pip install torch

  - installation de scipy est utilisé pour la fonction softmax, qui transforme les logits en probabilités (bash). : pip install scipy

  - Certains modèles nécessitent un compilateur Rust pour traiter des composants comme les tokenizers. Si nécessaire, installez Rust(bash) : curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

  -ensuite effectuer le chargement de données grace à pandas , le chargement du modele et du tokenizer , faire la tokenisation, et les predictions ( les avis sont traités par petits groupes et les scores brutes sont extraits du modeles) 

  -ensuite on ajoute kes prédiction au dataframe dans de nouvelle colones et on sauvegarde le resultat dans un nouveau fichier csv


    D- Creation de l'application streamlit 

  -Installation de Streamlit (bash) : pip install streamlit 

  -Installation de Matplotlib (bash) : pip install matplotlib 

  -importation des bibliotheque pandas, numpy, matplotlib, transformers et streamlit 

  -Le tokenizer décompose les textes en un format compréhensible par le modèle.

  -Traitement en lots : optimise la mémoire et le temps d'exécution.

  -Softmax : convertit les scores bruts du modèle en probabilités pour chaque classe.

  -Les sentiments (positif, négatif, neutre) sont déterminés par la classe ayant la probabilité maximale.

  -Creation de l'interface utilisateur Streamlit 

  -code pour charger le dataframe à analyser dans le dataframe 

  -creation des differents graphique 

  -Recomandation par rapport aux avis négatifs 

  -Telechargement des resultats enrichis 


    E- Hebergement de l'application dans StreamlitCloud 

  - Création du compte Streamlit Cloud et connexion au GitHub

  - lié notre compte GitHub à Streamlit Cloud en autorisant l'accès à nos dépôts via les paramètres de connexion de Streamlit Cloud.

  - Création du dépôt GitHub (KeyceM2Moume/Groupe9_DataCamp) pour y stocker le code source de notre application, y compris les fichiers nécessaires comme app.py, requirements.txt, et d'autres fichiers associés. 

  - Difficulté Rencontrée: La mise en place de fichiers spécifiques, comme requirements.txt, pouvait entraîner des erreurs si les dépendances n'étaient pas correctement listées.

  - Solution : soigneusement répertorié toutes les bibliothèques nécessaires (par exemple, streamlit, transformers, torch, pandas, etc.) dans le fichier requirements.txt.

  - Déploiement de l'application depuis GitHub

  - Difficulté rencontrée : Des erreurs liées à des dépendances manquantes ou des versions incompatibles de bibliothèques (par exemple, tokenizers nécessitant l'installation de Rust).

  - Solution : Nous avons mis à jour les bibliothèques dans le fichier requirements.txt et installé des outils additionnels (comme Rust) pour résoudre les problèmes de compilation, ce qui a permis de finaliser l'installation des dépendances.

  - Installation de Rust (bash) : Invoke-WebRequest -Uri https://sh.rustup.rs -OutFile rustup-init.exe; .\rustup-init.exe. Ensuite suivre les instructions d'installation et l'ajouter dans le PATH

  - Redemarer l'application 


2 - Acces à l'application 

  L'application est accessible à toutes personnes disposant du lien suivant :  https://groupe9datacamp-kpofbvqkesu68ba4wx7ltq.streamlit.app/


3 - How to use 

  l'utilisation de l'application est très simple 

-Cliquer sur le lien de l'application 

-Dans la fenetre "Drag and Drop files here" cliquer sur "Browse files" Pour selectionner un fichier csv à analyser 

-Selectionner la colonne contenant les commentaire , pour permettre aux graphiques dynamique de l'éviter car n'est pas pertinant pour les visualisations 

-Sélectionnez la colonne contenant les dates (si disponible) necessaire à la courbe d'évolution des sentiment en fonction des années 

-Clisquer sur télécharger les données pour sauvegarder les graphiques si besoin 
  



    

  

  

  
