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

# Create a Dictionary of the product list
totalProductList = []

###-----FORMATING DATA------
## Product name
## Product Price
## Product Saved Price
## Product Image
## Product Sortby
'''
    JSON format:
    {
        'product name': <String>,
        'product price': <Integer>,
        'product saved price': <Integer>,
        'product image url': <String>,
        'product sort group': <String>,
    }

'''

# Grabs product name 
productNames_info = page_soup.findAll("div", {"class": "details"})
productName = productNames_info[0].div.h2.a.text

# Grabs product price
productPrice_info = page_soup.findAll("span", {"itemprop": "price"})
productPrice = productPrice_info[0].text.split('$')[1]

# Grabs product saved price
productSavedPrice_info = page_soup.findAll("span", {"class": "savings"})
productSavedPrice = productSavedPrice_info[0].text.split('$')[1]

# Grabs product image url
productImage_info = page_soup.findAll("a", {"class": "image"})
productImage = productImage_info[0].find("img")['src']

# Grabs product group
productGroup_info = page_soup.findAll("div", {"class": "pre-dropdown Sort boosted"})
productGroup = productGroup_info[0].div.button.span.text



totalProductList = {
    "Product 1": {
        'Product name': productName,
        'Product price': productPrice,
        'Product saved price': productSavedPrice,
        'Product image url': productImage,
        'Product sort group': productGroup
    }
}

print(totalProductList)