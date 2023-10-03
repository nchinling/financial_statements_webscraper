import requests
from bs4 import BeautifulSoup
import pandas as pd

# Provide required url for income statement from Yahoo Finance
# url="https://sg.finance.yahoo.com/quote/<ticker>/<financials/cash-flow/balance-sheet>?p=<ticker>"
url="https://sg.finance.yahoo.com/quote/MSFT/financials?p=MSFT"
headers = {"User-Agent":"Chrome/117.0.5938.132"}
page=requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")

# create a dictionary to display income statement
statement = {}

# use BeautifulSoup to obtain specific data from html
# select the specific div class
table = soup.find_all("div", {"class":"W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)"})
for t in table:
    rows = t.find_all("div", {"class":"rw-expnded"})
    for row in rows:
        row_data = row.get_text(separator="|").split("|")
        statement[row_data[0]] = row_data[1]

statement_df = pd.DataFrame.from_dict(statement, orient='index', columns=['Value'])
print(statement_df.to_string())