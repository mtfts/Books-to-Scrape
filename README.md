# Web Scraping Books with Beautiful Soup

### Project Overview
In this project, we will be scraping a table from a website using Python and the pandas library. 
The website we will be scraping is a catalog of books with their prices and ratings. 
We will extract the data using the BeautifulSoup library and then save it to a Pandas DataFrame.

#### Tools used:

- Python 
- requests
- BeautifulSoup
- pandas

### Step-by-Step Guide
#### 1. Step 1: Importing the required libraries
![image](https://user-images.githubusercontent.com/86577716/223216763-92f7c96f-79bf-43fd-aa5e-cc1fe44285bb.png)

import requests: This imports the requests library, which is used to send HTTP requests in Python.

from bs4 import BeautifulSoup: This imports the BeautifulSoup class from the bs4 library, which is used to parse HTML documents and extract data from them.

import pandas as pd: This imports the pandas library and aliases it as pd, which is a commonly used alias for the library. pandas is a popular data manipulation library in Python that provides data structures like DataFrame for working with structured data.


#### 2.Step 2:  Scraping the data
![image](https://user-images.githubusercontent.com/86577716/223219098-3ade25b5-d1b1-4dbb-932a-df7c9c8024c8.png)

books = []: This creates an empty list called books that will be used to store the data that we scrape.

for i in range(1,51):: This sets up a for loop that will iterate through the pages of the website that we want to scrape. In this case, the loop will iterate through pages 1 to 50, inclusive.

url = f"https://books.toscrape.com/catalogue/page-{i}.html": This creates a variable called url that contains the URL of the page that we want to scrape. The f-string notation is used here to dynamically insert the value of i into the URL.

response = requests.get(url): This sends a GET request to the URL and stores the response object in the response variable.

response = response.content: This extracts the content of the response object and stores it in the response variable. This content is the HTML of the page that we want to scrape.

soup = BeautifulSoup(response, 'html.parser'): This creates a BeautifulSoup object called soup that parses the HTML of the page that we want to scrape.

ol = soup.find('ol'): This finds the first ol tag in the HTML of the page that we want to scrape and stores it in the ol variable. This tag contains all of the book listings on the page.

articles = ol.find_all('article', class_='product_pod'): This finds all of the article tags within the ol tag that have a class attribute of product_pod, which represents the individual book listings. These article tags are stored in the articles variable as a list.


#### Step 3: Extracting the relevant information
![image](https://user-images.githubusercontent.com/86577716/223219806-0a6f7cd5-b027-453c-9f10-b0f629addae0.png)

for article in articles: This is a for loop that iterates through all the articles (items) in the articles list.

image = article.find('img'): This finds the 'img' tag within each article and assigns it to the variable 'image'.

title = image.attrs['alt']: This extracts the value of the 'alt' attribute from the 'image' tag and assigns it to the variable 'title'.

star = article.find('p'): This finds the first 'p' tag within each article and assigns it to the variable 'star'.

star = star['class'][1]: This extracts the second class name from the 'class' attribute of the 'star' variable and assigns it back to the 'star' variable. This represents the star rating of the book.

price = article.find('p', class_='price_color').text: This finds the 'p' tag with a class of 'price_color' within each article and extracts its text, which represents the price of the book. The price is then assigned to the 'price' variable.

price = float(price[1:]): This converts the price to a float by removing the first character (which is the pound/dollar sign) and converting the remaining string to a float. The converted price is then assigned back to the 'price' variable.

books.append([title, price, star]): This appends a list of the book title, price, and star rating to the 'books' list. This list represents one row of data for the book DataFrame that will be created later.


#### Step 4: Creating a DataFrame

![image](https://user-images.githubusercontent.com/86577716/223220989-ba651842-31b9-4b29-9542-2215c854f373.png)

df = pd.DataFrame(books,columns=['Title', 'Price', 'Star Rating']): This line creates a DataFrame object called df using the pandas library. The pd.DataFrame() method takes the books list as input and creates a table with three columns - 'Title', 'Price', and 'Star Rating'. 
The columns parameter is used to specify the column names for the DataFrame.
