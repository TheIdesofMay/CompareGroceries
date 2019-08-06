# Shopping companion tool:

# * Input: the name of the product you want - either a specific brand of something or a more general item, such as chicken
# * The app will then go through a predefined list of stores (Tesco, Waitrose, Sainsburys etc..)
# * It’ll then search through them, extract the price of the item and the amount
# * Then show the price of the item 

# TODO:
# more shops


# how do we lay this out
# class SearchQ
# supermarket Class where the parameters you pass are the shopping centres you want to search 
# class Product(name) 

from bs4 import BeautifulSoup
import requests



class Tesco():

	sub_url = "https://www.tesco.com/groceries/en-GB/search?query="

	def __init__(self, product_name):

		self.product_name = product_name

	def get_product_info():

		search_token = product_name.replace(" ", "%20")
		url = sub_url+search_token
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


search_query = input("What would you like to search? \n")

search_initialisation = Tesco(search_query)

Tesco.get_product_info()


	


