# Question 2 – HTML Parsing & Data Extraction
# Topics Covered:
# Parsing HTML (BeautifulSoup, lxml), Web automation basics
# Write a Python program that:
# 1. Fetches an HTML webpage using the requests library
# 2. Parses the HTML using BeautifulSoup with the lxml parser
# 3.Extracts:
# Page title
# All hyperlinks
# Specific table or list data
# 4. Converts the extracted data into JSON format
# 5. Saves the output into a file for further automation or analysis

import requests
from bs4 import BeautifulSoup
import json


url="https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
soup = BeautifulSoup(response.content,"lxml")
pagetitle=soup.title.string if soup.title.string else "no title"

links=[]
for link in soup.find_all('a'):
    href=link.get('href')
    if href:
        links.append(href)
table_data=[]
table=soup.find("table")
if table:
    rows=table.find_all("tr")
    for row in rows[1:]:
        cols=row.find_all("td")
        table_data.append({
            "Company": cols[0].text.strip(),
            "Contact": cols[1].text.strip(),
            "Country": cols[2].text.strip()
        })
final_data={
    "Page_Title":pagetitle,
    "Total Links":len(links),
    "Links":links,
    "Table_Data":table_data
}
print(final_data)

with open("BeautifulSoup_data.json","w",encoding="utf-8") as file:
    json.dump(final_data,file,indent=4)
print("Data extracted and saved successfullu!")