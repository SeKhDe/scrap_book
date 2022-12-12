import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}
LIVRE_1 = "catalogue/the-black-maria_991/index.html"
def extraire_donnees(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

    infos_livre = [ "product_page_url", "upc"," title", "price_including_tax", "price_excluding_tax",
                    "number_available",  "product_description", "category", "review_rating", "image_url"]


    upc_table = soup.find("table" ,class_= "table")
    upc =  upc_table.find("td").text
    print(upc)




extraire_donnees(BASE_URL + LIVRE_1)
    