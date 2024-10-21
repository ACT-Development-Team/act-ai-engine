import yfinance as yf

def fetch_stock_data(company_name):
    stock = yf.Ticker(company_name)
    data = stock.history(periods="1d")
    return {
        "symbol": company_name,
        "price": data['Close'][-1],
        "high": data['High'][-1],
        "low": data['Low'][-1],
        "volume": data['Volume'][-1]
    }