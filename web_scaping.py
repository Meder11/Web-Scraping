import requests
from bs4 import BeautifulSoup

# Get the web page content

url = "https://books.toscrape.com/"
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# FInd all books on the page
books = soup.find_all('article', class_='product_pod')

# Loop through each book and extract the title and price
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f'Title: {title}, Price: {price}')

