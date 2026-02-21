# Write me a function which hepl me act as a tool which connects to yahoo finnance api and retires specific compnay details

import yfinance as yf

def get_company_details(ticker: str) -> dict:
    """Get company details from Yahoo Finance."""
    company = yf.Ticker(ticker)
    return company.info


# Can i get the output in a structubed formal for bettern understanding with stock price 

def get_company_details_structured(ticker: str) -> dict:
    """Get company details from Yahoo Finance in a structured format."""
    company = yf.Ticker(ticker)
    info = company.info
    return {
        "ticker": ticker,
        "company_name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "website": info.get("website"),
        "phone": info.get("phone"),
        "address": info.get("address"),
        "city": info.get("city"),
        "state": info.get("state"),
        "zip": info.get("zip"),
        "country": info.get("country"),
        "stock_price": info.get("currentPrice"),
    }   

if __name__ == "__main__":
    print(get_company_details_structured("HFCL.NS"))
