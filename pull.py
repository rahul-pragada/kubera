from nsetools import Nse

# Create an instance of Nse
nse = Nse()

# List of stock symbols
stocks = ["ABCAPITAL", "BIKAJI", "CARBORUNIV", "CASTROLIND"]

# Fetch and display LTP for each stock
for stock in stocks:
    try:
        quote = nse.get_quote(stock)
        print(f"{stock}: ₹{quote['lastPrice']}")
    except Exception as e:
        print(f"Could not fetch data for {stock}: {e}")


# code from anand