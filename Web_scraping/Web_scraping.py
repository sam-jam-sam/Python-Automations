import requests
from bs4 import BeautifulSoup

page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")

soup = BeautifulSoup(page.content, 'html.parser')

top_items = []

products = soup.select('div.thumbnail')
for elemnts in products:
    title = element