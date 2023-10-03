from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def display_income_statement():
    if request.method == 'POST':
        # Get ticker and statement_type from the submitted form
        ticker = request.form.get('ticker', 'MSFT')
        statement_type = request.form.get('statement_type', 'financials')
    else:
        # Get ticker and statement_type from URL parameters
        ticker = request.args.get('ticker', 'MSFT')
        statement_type = request.args.get('statement_type', 'financials')

    # Construct the URL based on the ticker and statement_type
    url = f"https://sg.finance.yahoo.com/quote/{ticker}/{statement_type}?p={ticker}"
    headers = {"User-Agent": "Chrome/117.0.5938.132"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")

    # Create a dictionary to store the income statement
    statement = {}

    # Use BeautifulSoup to obtain specific data from HTML
    # Select the specific div class
    table = soup.find_all("div", {"class": "W(100%) Whs(nw) Ovx(a) BdT Bdtc($seperatorColor)"})
    for t in table:
        rows = t.find_all("div", {"class": "rw-expnded"})
        for row in rows:
            row_data = row.get_text(separator="|").split("|")
            statement[row_data[0]] = row_data[1]

    statement_df = pd.DataFrame.from_dict(statement, orient='index', columns=['Value'])

    # Render an HTML template with the data
    return render_template('statement.html', table=statement_df.to_html(classes='table table-striped'))

if __name__ == '__main__':
    app.run(debug=True)

