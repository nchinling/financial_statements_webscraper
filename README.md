# Financial Statements (web-scraping)

## Overview

This Flask web application allows users to retrieve financial statements for a specified stock ticker symbol. The app utilizes web scraping techniques to extract financial data from Yahoo Finance. Users can obtain financial statements (cash-flow, balance sheets and income statement). 

## Current Features

The financial web scraping app includes the following features:

1. **Retrieve Financial Statements**: Users can enter a stock ticker symbol and select a statement type (Financials, Cash Flow, or Balance Sheet) to retrieve and display the corresponding financial statement.

2. **Display in Table Format**: The financial statement data is displayed in a table format within the web application.

3. **User Interface**: The app provides a simple user interface where users can input the stock ticker symbol and select the statement type through a form.


4. **URL Construction and Web Scraping**: The code constructs a URL based on user input and uses web scraping techniques (with BeautifulSoup) to extract financial data from Yahoo Finance.


5. **Error Handling**: It provides a default message ("Provide a ticker") if a ticker is not provided.

These features provide a foundation for retrieving and displaying financial data, with room for additional enhancements based on user needs and future development goals.


## Technologies Used

- API
- Pandas
- BeautifulSoup for web-scraping
- Flask

## Installation

git clone <repository-url>
cd <directory>


## Usage

python app.py
Open your web browser and go to http://127.0.0.1:5000/





