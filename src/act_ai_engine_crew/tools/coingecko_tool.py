import requests
from typing import Dict
from pydantic import BaseModel


class CoinGeckoTool(BaseModel):
    name: str = "coingecko_tool"
    description: str = "CoinGecko tool"

    def fetch_crypto_data(symbol):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if symbol in data:
                return {
                    "symbol": symbol,
                    "price": data[symbol]['usd'],
                    "change_24h": data[symbol].get('usd_24h_change', 'N/A')
                }
        return {"error": "Couldnt fetch data"}