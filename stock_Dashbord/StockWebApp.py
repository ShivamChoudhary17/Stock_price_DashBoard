from altair.vegalite.v4.schema.core import Header
from numpy import imag
import streamlit as st
import pandas as pd
from PIL import Image


st.write("""
# Stock Market Web Application\n
** Visually ** show Data on a stock! of Amazon, Google, Microsoft, Netflix, TCS, FB
""")

image = Image.open("D:/Python_project/stock_Dashbord/download.jpg")
st.image(image, use_column_width=True)

#Create sidebar
st.sidebar.header('User Input')

#Create a function to get the User Imput
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-06-29")
    end_date = st.sidebar.text_input("End Date", "2021-06-25")
    Stock_Symbol = st.sidebar.text_input("Stock_Symbol", "AMZN")
    return start_date, end_date, Stock_Symbol

#Create a function to get company name
def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'GOOG':
        return 'Google'
    elif symbol == 'NFLX':
        return 'Netflix'
    elif symbol == 'FB':
        return 'FaceBook'
    elif symbol == 'TCS':
        return 'TCS'
    elif symbol == 'MSFT':
        return 'Microsoft'
    else:
        'None'

#Create function to get proper data and time frame
def get_data(symbol, start, end):
    #Load data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("D:/Python_project/stock_Dashbord/stocks/AMZN.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("D:/Python_project/stock_Dashbord/stocks/GOOG.csv")
    elif symbol.upper() == 'NFLX':
        df = pd.read_csv("D:/Python_project/stock_Dashbord/stocks/NFLX.csv")
    elif symbol.upper() == 'TCS':
        df = pd.read_csv("D:/Python_project/stock_Dashbord/stocks/TCS.csv")
    elif symbol.upper() == 'MSFT':
        df = pd.read_csv("D:/Python_project/stock_Dashbord/stocks/MSFT.csv")
    elif symbol.upper() == 'FB':
        df = pd.read_csv("D:/Python_project/stock_Dashbord/stocks/FB.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])
    
    #get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #Set the start and end index row to 0
    start_row = 0
    end_row = 0

    #Start looking at date from top to down to see if start <= date end
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row =  i
            break

    #satrt from bottom to top
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df) - 1 - j]):
            end_row = len(df) - 1 - j
            break

    # Set index to date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row + 1, :]

#get the user input
start, end, symbol = get_input()
#get the data
df = get_data(symbol, start, end)
#get the company name
company_name = get_company_name(symbol.upper())

#Display the Close Price
st.header(company_name + " Close Price\n")
st.line_chart(df['Close'])

st.header(company_name + " Volume\n")
st.line_chart(df['Volume'])

# Get some statistics on data
st.header('Data Statistics')
st.write(df.describe())