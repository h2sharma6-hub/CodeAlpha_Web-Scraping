# CodeAlpha_Web-Scraping
In this task, I created a web scraping project using Python. The objective was to extract motivational quotes along with their authors from a website and store them in a structured dataset.

Steps :

Imported libraries
requests to send HTTP requests and fetch the web page.

BeautifulSoup to parse and extract HTML content.

pandas to organize the data and save it into a CSV file.

Fetched website data
Used the site http://quotes.toscrape.com/ for collecting sample quotes.

Parsed the HTML
Extracted all the text inside for quotes.

Extracted all the text inside for authors.

Stored the data
Saved the extracted data in two lists: quotes[] and authors[].

Converted them into a pandas DataFrame.

Created dataset
Exported the data into a CSV file named quotes.csv.

The dataset contains two columns: Quote and Author.

Output

A structured CSV dataset of motivational quotes.

Example record:

Quote Author

“The world as we have created it is a process of our thinking...” Albert Einstein
