import yfinance as yf
from typing import Dict, Any
from pydantic import BaseModel, Field

class YahooFinance(BaseModel):
    name: str = Field(default="yahoo_finance_tool")
    description: str = Field(default="Yahoo Finance tool")

    def fetch_stock_data(self, company_name: str) -> Dict[str, Any]:
        stock = yf.Ticker(company_name)
        data = stock.history(periods="1d")
        return {
            "symbol": company_name,
            "price": data['Close'][-1],
            "high": data['High'][-1],
            "low": data['Low'][-1],
            "volume": data['Volume'][-1]
        }
    
    def invoke(self, company_name: str) -> Dict[str, Any]:
        """Invoke the tool to fetch stock data for a given company."""
        return self.fetch_stock_data(company_name)
