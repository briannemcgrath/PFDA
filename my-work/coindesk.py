import requests

url ="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

#Access the current price in Euros
euro_price = data['bpi']['EUR']['rate']

print(f"Current price in Euros: {euro_price}")