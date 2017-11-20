import json
from helper_functions import clean_ticker

def lookup_ticker(t):
    with open("symbols.json") as f:
        ticker_symbols = json.load(f)
    try:
        print("Company name:", ticker_symbols[t])
    except KeyError:
        print("Invalid ticker symbol. Exiting...")

if __name__ == '__main__':
    while True:
        ticker_input = clean_ticker(input("Enter a ticker symbol (enter q to quit): "))
        if ticker_input == "q":
            break
        lookup_ticker(ticker_input)