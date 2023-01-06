# scrap_book
***Description du projet***

Ce script Python est conçu pour extraire des données de livres à partir du site Web  "books.toscrape.com" et les stocker dans des fichiers CSV pour une utilisation 
ultérieure. Il comprend plusieurs fonctions qui sont utilisées pour effectuer des requêtes HTTP sur le site, parser le contenu HTML des pages et extraire les données 
de chaque livre.


***Prérequis***

Pour utiliser ce script, vous aurez besoin de:

    Un ordinateur avec Python 3 installé
    Les modules Python suivants: requests, BeautifulSoup4, csv et os
    

***Utilisation avec un environnement virtuel***

Voici comment utiliser ce code dans un environnement virtuel :

    Créez un nouvel environnement virtuel en utilisant la commande virtualenv mon_env. Remplacez mon_env par le nom de votre choix pour l'environnement virtuel.

    Activez l'environnement virtuel en utilisant la commande source mon_env/bin/activate (Linux/Mac) ou mon_env\Scripts\activate.bat (Windows). Remplacez mon_env par le nom de votre environnement virtuel.

    Installez les bibliothèques nécessaires en utilisant pip install -r requirements.txt. Si vous n'avez pas encore de fichier requirements.txt, vous pouvez le créer en exécutant pip freeze > requirements.txt une fois les bibliothèques installées.

    Lancez le processus de scraping en exécutant le code Python avec votre interpréteur de commandes.

***Installation et configuration*** 

Pour utiliser ce script, suivez les étapes suivantes:

   - Téléchargez le fichier book_scraper.py sur votre ordinateur
   - Ouvrez un terminal et accédez au dossier où vous avez téléchargé le fichier
   - Assurez-vous d'avoir installé les modules Python requis (requests, BeautifulSoup4, csv)
   - Exécutez le script en utilisant la commande python book_scraper.py

***Utilisation***

Une fois le script exécuté, il effectuera une série de requêtes HTTP sur le site "books.toscrape.com" et extraira les données de chaque livre de chaque catégorie de 
livres. Les données seront enregistrées dans des fichiers CSV avec le nom de la catégorie de livres comme nom de fichier. 
Les fichiers CSV seront enregistrés dans un dossier nommé "data_site" à l'emplacement où se trouve le script.
