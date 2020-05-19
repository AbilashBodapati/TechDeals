'''
    File name: webScrapper.py
    Author name: Abilash Bodapati
    Description: This is a script that scraps data from websites to get tech deals.
'''

# Import all the necessary libraries
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

# URL I want to initially scrap. Intel CPU page
microcenter_url = ['https://www.microcenter.com/search/search_results.aspx?N=4294966995+4294820689&sortby=rating',
                   'https://www.microcenter.com/search/search_results.aspx?N=4294966995+4294820689&sortby=match',
                   'https://www.microcenter.com/search/search_results.aspx?N=4294966995+4294820689&sortby=pricehigh']


# Create a dictionary of the product dictionaries
totalProductList = []

for url in microcenter_url:
    # query the website and return the html to the variable 'page'
    uClient = uReq(url)

    # Raw html page of the Intel CPU results page
    page_html = uClient.read()

    # Close the uClient Connection to the website.
    uClient.close()

    # HTML parsing
    page_soup = soup(page_html, "html.parser")

    ###-----FORMATING DATA------
    ## Product name
    ## Product Price
    ## Product Saved Price
    ## Product Image
    ## Product Group by
    ## Product Retrevied from
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
    # Grabs product price
    productPrice_info = page_soup.findAll("span", {"itemprop": "price"})
    # Grabs product saved price
    productSavedPrice_info = page_soup.findAll("span", {"class": "savings"})
    # Grabs product image url
    productImage_info = page_soup.findAll("a", {"class": "image"})

    # Grabs product group
    productGroup_info = page_soup.findAll("div", {"class": "pre-dropdown Sort boosted"})
    # Product Group By
    productGroup = productGroup_info[0].div.button.span.text

    # A for-loop to iterate through the list created above
    for i in range(10):
        # Product Name
        productName = productNames_info[i].div.h2.a.text
        # Product Price
        productPrice = productPrice_info[i].text.split('$')[1]
        # product Saved Price
        productSavedPrice = productSavedPrice_info[i].text.split('$')[1]
        # Product Image URL
        productImage = productImage_info[i].find("img")['src']
        
        productIter = '{} Product {}'.format(productGroup, i+1)
        # Add the product in to the list
        productDict = {
            'Productname': productName,
            'Productprice': productPrice,
            'Productsavedprice': productSavedPrice,
            'Productimageurl': productImage,
            'Productsortgroup': productGroup
        }

        # Append the created dictionary to the total list
        totalProductList.append(productDict)


# Creating a JSON file
jsonFormatedProductList = json.dumps(totalProductList, indent=4)

print(jsonFormatedProductList)

# Writing to sample.json 
with open("products.json", "w") as outfile: 
    outfile.write(jsonFormatedProductList)