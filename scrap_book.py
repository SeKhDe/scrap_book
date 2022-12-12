import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com"
HEADERS = {User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"}

def extraire_donnees(url):
    response = requests.get(url, headers=HEADERS)
    