import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv



BASE_URL = "http://books.toscrape.com/"
BASE_URL_category = "http://books.toscrape.com/catalogue/"
url_fiction = "http://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
url_romance = "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
url_travel = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
url_mistery = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
url_book_sharp = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
#Fonction extraction d'une categorie

def extract_category(url):

    page = True
    i = 1
    liste_url_category = []
    extr = []
    while page:
        url_category = url
        response = requests.get(url_category)
        if response.status_code == 200:

            html = response.content
            soup = BeautifulSoup(html, "html.parser")

            if i == 1:
                url = url.rstrip("index.html")
                url = url + f"page-{i+1}.html"
            else:
                index = url.index("page")
                url = url[:index]
                url += f"page-{i}.html"


            i+= 1


            ol_class = soup.find("ol", class_="row")
            li_class = ol_class.find_all("li", class_="col-xs-6")
            for li in li_class:
                a = li.find("a")
                a = BASE_URL_category + a["href"].replace("../../../", "")
                if not a in liste_url_category:
                   liste_url_category.append(a)
                   ex = extract_book(a)
                   extr.append(ex)




        else:
            page = False


    return extr





#Fonction extraction d'un livre
def extract_book(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

    product_page_url = url

    table = soup.find("table", class_="table")
    upc = table.find("td").text

    title = soup.find("h1").text

    table = soup.find("table", class_="table table-striped")
    tds = table.find_all("td")
    price_including_tax = tds[3].text

    price_excluding_tax = tds[2].text

    number_available = tds[5].text

    product_description_article = soup.find("article", class_="product_page")
    product_description = product_description_article.find("p", recursive=None).text

    ul_breadcrumb = soup.find("ul", class_="breadcrumb")
    categorys = ul_breadcrumb.find_all("li")
    category = categorys[2].text.strip("\n")

    div_product = soup.find("div", class_="product_main")
    p_start_rating = div_product.find("p", class_="star-rating")
    review_rating = p_start_rating.attrs["class"][1]

    div_item = soup.find("div", class_="item")
    balise_img = div_item.find("img")
    image_url_src = balise_img["src"]
    image_url = image_url_src.replace("../../", BASE_URL_category)

    en_tete = ["product_page_url","upc","title","price_including_tax","price_excluding_tax","number_available",
               "category","review_rating","image_url","product_description"]

    infos_livre = [product_page_url, upc, title,
                    price_including_tax, price_excluding_tax,number_available,
                    category,review_rating,
                   image_url, product_description]



    return infos_livre

infos_book = extract_book(url_book_sharp)
infos_category = extract_category(url_travel)

en_tete = ["product_page_url","upc","title","price_including_tax","price_excluding_tax","number_available",
               "category","review_rating","image_url","product_description"]

with open("dat.csv","w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(en_tete)

    for a,b,c,d,e,f,g,h,i,j in infos_category:

        ligne = [a,b,c,d,e,f,g,h,i,j]
        writer.writerow(ligne)
