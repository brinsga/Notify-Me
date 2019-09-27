# Importing the required modules

import requests
import json
import configparser

#reading config file
config = configparser.ConfigParser()
config.read("config.ini")

#constructing API endpoint request URL
nyc_api_url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=" + str(config['nycdev']['apikey'])

#sending requests & printing error code
response = requests.get(nyc_api_url)
print(response.status_code)

top15books = []
top15author = []

#Getting the top15 books and their author
def gettop15():
	booklist = response.json()['results']['books']
	for books in booklist:
		top15books.append(books['title'])
		top15author.append(books['author'])

#printing the top 15 books and their authors
#this is a current test function
def print_top_15_nyc_bestseller():
	for i in range(0,len(top15books)):
		print(str(i+1) + ". " + str(top15books[i]) + " - " + str(top15author[i]))

#function calls
gettop15()
print_top_15_nyc_bestseller()


