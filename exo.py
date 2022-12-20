import requests
from bs4 import BeautifulSoup
import pandas as pd



BASE_URL = "http://books.toscrape.com/"
BASE_URL_category = "http://books.toscrape.com/catalogue/"
url_fiction = "http://books.toscrape.com/catalogue/category/books/fiction_10/"



#Fonction extraction d'une categorie

def extract_category(url):
    page = True
    i = 1
    liste_url_category = []
    extr = []
    while page:
        url_category = f"{url}page-{i}.html"
        response = requests.get(url_category)
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, "html.parser")
            i += 1
        else:
            page = False



        ol_class = soup.find("ol", class_="row")
        li_class = ol_class.find_all("li", class_="col-xs-6")
        for li in li_class:
            a = li.find("a")
            a = BASE_URL_category + a["href"].replace("../../../", "")
            if not a in liste_url_category:
                liste_url_category.append(a)


        for url_page in liste_url_category:
            ex = extract_book(url_page)
            extr.append(ex)



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
    product_description = product_description_article.find("p", recursive=None)

    ul_breadcrumb = soup.find("ul", class_="breadcrumb")
    categorys = ul_breadcrumb.find_all("li")
    category = categorys[2].text

    div_product = soup.find("div", class_="product_main")
    p_start_rating = div_product.find("p", class_="star-rating")
    review_rating = p_start_rating.attrs["class"][1]

    div_item = soup.find("div", class_="item")
    balise_img = div_item.find("img")
    image_url_src = balise_img["src"]
    image_url = image_url_src.replace("../../", BASE_URL_category)

    infos_livre = {"product_page_url": product_page_url, "upc": upc, "title": title,
                   "price_including_tax": price_including_tax, "price_excluding_tax": price_excluding_tax,
                   "number_available": number_available, "product_description": product_description,
                   "category": category, "review_rating": review_rating,
                   "image_url": image_url}


    return infos_livre



