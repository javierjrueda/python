import requests
import time
import json
from datetime import datetime

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/test_event/with/key/n3RGiAGRIUr9OVaPBl-3l7vWdYhNT7nPjKxOhT7PCE4'

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    return float(response_json[0]['price_usd'])  # Convert the price to a floating point number

def main():
    price = get_latest_bitcoin_price()
    date = datetime.now()
    
    requests.post(IFTTT_WEBHOOKS_URL)

    time.sleep(45)  # Sleep for 5 minutes (for testing purposes you can set it to a lower number)

if __name__ == '__main__':
    main()