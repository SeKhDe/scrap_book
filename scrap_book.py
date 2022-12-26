import requests
from bs4 import BeautifulSoup
import csv
import os
# coding: <encoding>


BASE_URL = "http://books.toscrape.com/"
BASE_URL_category = "http://books.toscrape.com/catalogue/"
url_fiction = "http://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
url_romance = "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
url_travel = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
url_mistery = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
url_book_sharp = "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"


#----------------------Fonction extraction site ---------------------------------------------
def extract_site():
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_available",
               "category", "review_rating", "image_url", "product_description"]

    url = "http://books.toscrape.com/"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

    else:
        return print(f"Erreur de la requete numero {response.status_code}")


    liste_liens_category = []
    extract_total = []
    site_categories = soup.find("div", class_="side_categories")
    ul_side_categories = site_categories.find("ul", class_="nav")
    ul_ = ul_side_categories.find("ul")
    li_ = ul_.find_all("li")
    for li in li_:

        a_ = li.find("a")
        a_ = a_["href"]

        liste_liens_category.append(url + a_)
    for liste in liste_liens_category:

        ext = extract_category(liste)
        nom_fichier = liste.split("/")[6]
        extract_total.append(ext)

        os.makedirs("data_site", exist_ok=True)
        with open(f"data_site\{nom_fichier}.csv", "w", encoding="utf-8") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(en_tete)
            for ligne in ext:
                writer.writerow(ligne)



    return extract_total


#----------------------Fonction extraction d'une categorie---------------------------------------
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





#------------------------Fonction extraction d'un livre----------------------------------------
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
    product_description = str(product_description_article.find("p", recursive=None))
    product_description = product_description.strip("<\p>")


    ul_breadcrumb = soup.find("ul", class_="breadcrumb")
    categorys = ul_breadcrumb.find_all("li")
    category = categorys[2].text.strip("\n")

    div_product = soup.find("div", class_="product_main")
    p_start_rating = div_product.find("p", class_="star-rating")
    review_rating = p_start_rating.attrs["class"][1]

    div_item = soup.find("div", class_="item")
    balise_img = div_item.find("img")
    image_url_src = balise_img["src"]
    image_url = image_url_src.replace("../../", BASE_URL)



    infos_livre = [product_page_url, upc, title,
                    price_including_tax, price_excluding_tax,number_available,
                    category,review_rating,
                   image_url, product_description]




    return infos_livre


infos_cate = extract_site()


