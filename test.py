import requests
from bs4 import BeautifulSoup
import pandas as pd


HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}
BASE_URL = "http://books.toscrape.com/"
BASE_URL_category = "http://books.toscrape.com/catalogue/"

urls_category_fiction = []
url = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-1.html"

product_page_url_s = []
upcs = []
titles = []
price_including_tax_s = []
price_excluding_tax_s = []
number_available_s = []
product_description_s = []
category_s= []
review_rating_s = []
image_url_s= []
liste_url = []

#recuperation de la liste des categories
url_site = "http://books.toscrape.com/index.html"
reponse_requete = requests.get(url_site)

soup_1 = BeautifulSoup(reponse_requete.content, "html.parser")

liste_liens_categorie = []
site_categories = soup_1.find("div", class_="side_categories")
ul_side_categories = site_categories.find("ul", class_="nav")
ul_ = ul_side_categories.find("ul")
li_ = ul_.find_all("li")
for li in li_:
    a_ = li.find("a")
    a_ = a_["href"].strip("index.html")
    liste_liens_categorie.append(BASE_URL + a_)


for url in liste_liens_categorie:
    for i in range(1,50):
        url_categorie_ = f"{url}page-{i}.html"
        response = requests.get(url_categorie_)
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, "html.parser")
        else:
            break





        li_class = soup.find("ol", class_="row").find_all("li","col-xs-6")
        for li in li_class:
            a = li.find("a")
            a = BASE_URL_category + a["href"].replace("../../../", "")

            liste_url.append(a)

        for book_url in liste_url:
            response = requests.get(book_url)
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, "html.parser")


        product_page_url_s.append(book_url)


        table = soup.find("table", class_="table")
        upc = table.find("td").text
        upcs.append(upc)

        title = soup.find("h1").text
        titles.append(title)

        table = soup.find("table", class_="table table-striped")
        tds = table.find_all("td")
        price_including_tax = tds[3].text
        price_including_tax_s.append(price_including_tax)

        price_excluding_tax = tds[2].text
        price_excluding_tax_s.append(price_excluding_tax)

        number_available = tds[5].text
        number_available_s.append(number_available)

        product_description_article = soup.find("article", class_="product_page")
        product_description = product_description_article.find("p", recursive=None)
        product_description_s.append(product_description)

        ul_breadcrumb = soup.find("ul", class_="breadcrumb")
        categorys = ul_breadcrumb.find_all("li")
        category = categorys[2].text
        category_s.append(category)

        div_product = soup.find("div", class_="product_main")
        p_start_rating = div_product.find("p", class_="star-rating")
        review_rating = p_start_rating.attrs["class"][1]
        review_rating_s.append(review_rating)

        div_item = soup.find("div", class_="item")
        balise_img = div_item.find("img")
        image_url_src = balise_img["src"]
        image_url = image_url_src.replace("../../", BASE_URL_category)
        image_url_s.append(image_url)

        infos_livre = {"product_page_url": product_page_url_s,"upc": upcs, "title": titles, "price_including_tax": price_including_tax_s, "price_excluding_tax": price_excluding_tax_s,
                       "number_available": number_available_s, "product_description": product_description_s, "category": category_s, "review_rating":  review_rating_s,
                       "image_url": image_url_s}



print(len(titles))
print(titles)
print()
print(len(product_page_url_s))
print(product_page_url_s)
print()
print(len(upcs))
print(upcs)
print()
print(len(price_excluding_tax_s))
print(price_excluding_tax_s)
print()
print(len(number_available_s))
print(number_available_s)
print()
print(len(category_s))
print(category_s)
print()
print(len(review_rating_s))
print(review_rating_s)
print()