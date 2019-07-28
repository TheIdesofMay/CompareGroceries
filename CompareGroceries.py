# Shopping companion tool:

# * Input: the name of the product you want - either a specific brand of something or a more general item, such as chicken
# * The app will then go through a predefined list of stores (Tesco, Waitrose, Sainsburys etc..)
# * It’ll then search through them, extract the price of the item and the amount
# * Then show the price of the item 

# TODO:
# more shops


from bs4 import BeautifulSoup
import requests

product_name = []
prices = []

search_token = input("What item would you like to search the Tesco website?: \n").replace(" ", "%20")



url = "https://www.tesco.com/groceries/en-GB/search?query=" + search_token

# parse webpage with search token
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

# find price per quantity weight and item name for each element on the webpage
prices_soup = soup.find_all('div', class_="price-per-quantity-weight")
product_names_soup = soup.find_all('a', class_="sc-htoDjs kRdgZa")

# convert html element to text
for item in product_names_soup:
	product_name.append(str(item.text))
for item in prices_soup:
	prices.append(str(item.text))

# change everything to price per kg. if it's in per 100g, multiple it by 10. 

# need to use regex to ensure that all of the values are in /kg from the beginning instead of doing some text processing bs before the print statment 

# combine product name and price into a dict
products_dict = dict(zip(product_name, prices))

for i in products_dict:
	print(i + ": " + products_dict[i])


