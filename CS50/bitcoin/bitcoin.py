import requests
import sys
import json

try:

    bitcoin = float(sys.argv[1])

    api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = api.json()
    rate = (data ["bpi"] ["USD"] ["rate"]).replace(",", "")
    value = float(rate)
    amount = bitcoin*value
    print(f"${amount:,.4f}")

except requests.RequestException:
    print ("Not valid value")

