import csv
def load_file_book(extract):
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_available",
               "category", "review_rating", "image_url", "product_description"]
    with open("data_book\data.csv", "w") as f:
        writer = csv.writer(f,delimiter=",")
        writer.writerow(en_tete)
        writer.writerow(extract)

def load_file_category(extract):
    en_tete = ["product_page_url", "upc", "title", "price_including_tax", "price_excluding_tax", "number_available",
               "category", "review_rating", "image_url", "product_description"]
    with open("data_category\data.csv","w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(en_tete)

        for a,b,c,d,e,f,g,h,i,j in extract:

            ligne = [a,b,c,d,e,f,g,h,i,j]
            writer.writerow(ligne)


