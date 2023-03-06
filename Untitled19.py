#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[24]:


books = []
for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, price, star])
         


# In[27]:


df = pd.DataFrame(books,columns=['Title', 'Price', 'Star Rating'])


# In[29]:


df.head(50)


# In[ ]:




