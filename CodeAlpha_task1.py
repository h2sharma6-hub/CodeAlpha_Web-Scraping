# Library import
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website from where data is collected
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Parsing the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Lists for storing data
quotes = []
authors = []

# Extracting quotes
for q in soup.find_all("span", class_="text"):
    quotes.append(q.text)

# Extracting authors
for a in soup.find_all("small", class_="author"):
    authors.append(a.text)

# Creating DataFrame
df = pd.DataFrame({"Quote": quotes, "Author": authors})

# Saving dataset
df.to_csv("quotes.csv", index=False)
print("Quotes dataset done. Total records:", len(df))

print(df.head())
