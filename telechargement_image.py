import requests
from bs4 import BeautifulSoup




def telechargement_img(url)
    for book in extract_category(url):
        url_img = book[8]
        response = requests.get(url_img)
#decoupe l'url et recupere la derniere parti pour en faire le nom de l'image
        nom_img = url_img.split("/")[-1]
        if response.status_code == 200:
            with open(f"image\{nom_img}","wb") as f:
                f.write(response.content)

    return