import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}

response = requests.get(BASE_URL)
parser = BeautifulSoup(response.content, "html.parser")
h3 = parser.find_all("h3")
a = h3[9].find("a")
product_page_url = a["href"]


def extraire_donnees(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

    en_tete = ["product_page_url", "upc", " title", "price_including_tax", "price_excluding_tax",
                   "number_available", "product_description", "category", "review_rating", "image_url"]




    table = soup.find("table" ,class_= "table")
    upc =  table.find("td").text


    title = soup.find("h1").text


    table = soup.find("table", class_="table table-striped")
    tds = table.find_all("td")
    price_including_tax= tds[3].text
    

    price_excluding_tax = tds[2].text

    number_available = tds[5].text

    product_description_article = soup.find("article", class_="product_page")
    product_description = product_description_article.find("p",recursive=None).text

    ul_breadcrumb = soup.find("ul", class_="breadcrumb")
    categorys = ul_breadcrumb.find_all("li")
    category = categorys[2].text


    div_product = soup.find("div",class_="product_main")
    p_start_rating = div_product.find("p", class_="star-rating")
    review_rating = p_start_rating.attrs["class"][1]


    div_item = soup.find("div", class_="item")
    balise_img = div_item.find("img")
    image_url_src = balise_img["src"]
    image_url = image_url_src.replace("../../", BASE_URL)



    infos_livre = [ product_page_url, upc, title, price_including_tax, price_excluding_tax,
                    number_available,  product_description, category, review_rating, image_url]


extraire_donnees(BASE_URL + product_page_url)



    