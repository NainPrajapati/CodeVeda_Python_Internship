# Level 2 - Task 3
# API Integration using CoinGecko API
# Codveda Python Internship

import requests


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "inr",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        print("\n===== Cryptocurrency Market Data (INR) =====\n")

        for coin in data:
            print(f"Name           : {coin['name']}")
            print(f"Symbol         : {coin['symbol'].upper()}")
            print(f"Price (INR)    : ₹{coin['current_price']}")
            print(f"Market Cap    : ₹{coin['market_cap']}")
            print(f"24h Change    : {coin['price_change_percentage_24h']}%")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data from API:", e)
    except KeyError:
        print("❌ Unexpected response format.")
    except Exception as e:
        print("❌ An unexpected error occurred:", e)


# Program execution starts here
fetch_crypto_data()
