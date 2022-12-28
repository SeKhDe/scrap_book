# scrap_book
***Description du projet***

Ce script Python est conçu pour extraire des données de livres à partir du site Web  "books.toscrape.com" et les stocker dans des fichiers CSV pour une utilisation 
ultérieure. Il comprend plusieurs fonctions qui sont utilisées pour effectuer des requêtes HTTP sur le site, parser le contenu HTML des pages et extraire les données 
de chaque livre.


***Prérequis***

Pour utiliser ce script, vous aurez besoin de:

    Un ordinateur avec Python 3 installé
    Les modules Python suivants: requests, BeautifulSoup4, csv et os
    
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
