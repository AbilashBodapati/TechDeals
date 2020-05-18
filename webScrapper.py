'''
    File name: webScrapper.py
    Author name: Abilash Bodapati
    Description: <TO BE WRITTEN AT THE END>
'''

# Import all the necessary libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# URL I want to initially scrap. Intel CPU page
microcenter_url = 'https://www.microcenter.com/search/search_results.aspx?N=4294966995+4294820689&sortby=rating'

# query the website and return the html to the variable 'page'
uClient = uReq(microcenter_url)

# Raw html page of the Intel CPU results page
page_html = uClient.read()

# Close the uClient Connection to the website.
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")
# Grabs all the products 
products_info = page_soup.findAll("div", {"class": "pDescription compressedNormal2"})
# CPU highest Rated
cpuProduct = products_info[0].div.h2.a.text

print(cpuProduct)