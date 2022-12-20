import requests
from bs4 import BeautifulSoup
import pandas as pd



BASE_URL = "http://books.toscrape.com/"
BASE_URL_category = "http://books.toscrape.com/catalogue/"
url_fiction = "http://books.toscrape.com/catalogue/category/books/fiction_10/"

product_page_url_s = []

#Fonction extraction d'une categorie

def extract_category(url):
    page = True
    i = 1
    liste_url_category = []
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




    return liste_url_category





#Fonction extraction d'un livre
def extract_book(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

    upcs = []
    table = soup.find("table", class_="table")
    upc = table.find("td").text
    upcs.append(upc)

    titles = []
    title = soup.find("h1").text
    titles.append(title)

    price_including_tax_s = []
    table = soup.find("table", class_="table table-striped")
    tds = table.find_all("td")
    price_including_tax = tds[3].text
    price_including_tax_s.append(price_including_tax)

    price_excluding_tax_s = []
    price_excluding_tax = tds[2].text
    price_excluding_tax_s.append(price_excluding_tax)

    number_available_s = []
    number_available = tds[5].text
    number_available_s.append(number_available)

    product_description_s = []
    product_description_article = soup.find("article", class_="product_page")
    product_description = product_description_article.find("p", recursive=None)
    product_description_s.append(product_description)

    category_s = []
    ul_breadcrumb = soup.find("ul", class_="breadcrumb")
    categorys = ul_breadcrumb.find_all("li")
    category = categorys[2].text
    category_s.append(category)

    review_rating_s = []
    div_product = soup.find("div", class_="product_main")
    p_start_rating = div_product.find("p", class_="star-rating")
    review_rating = p_start_rating.attrs["class"][1]
    review_rating_s.append(review_rating)

    image_url_s = []
    div_item = soup.find("div", class_="item")
    balise_img = div_item.find("img")
    image_url_src = balise_img["src"]
    image_url = image_url_src.replace("../../", BASE_URL_category)
    image_url_s.append(image_url)

    infos_livre = {"product_page_url": product_page_url_s, "upc": upcs, "title": titles,
                   "price_including_tax": price_including_tax_s, "price_excluding_tax": price_excluding_tax_s,
                   "number_available": number_available_s, "product_description": product_description_s,
                   "category": category_s, "review_rating": review_rating_s,
                   "image_url": image_url_s}


    return infos_livre


#print(extract_book("http://books.toscrape.com/catalogue/when-im-gone_95/index.html"))
print(len(extract_category(url_fiction)))
print(extract_category(url_fiction))