import yfinance as yf
import json
from app.utils.logger import logger

def get_company_details(ticker: str) -> dict:
    """Fetch comprehensive market data for a given stock ticker."""
    try:
        logger.info(f"Fetching data for ticker: {ticker}")
        company = yf.Ticker(ticker)
        info = company.info
        
        if not info or 'longName' not in info:
            return {"error": f"No data found for ticker: {ticker}"}

        data = {
            "ticker": ticker,
            "company_name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "stock_price": info.get("currentPrice") or info.get("regularMarketPrice"),
        }
        return data
    except Exception as e:
        logger.error(f"Error fetching data for {ticker}: {str(e)}")
        return {"error": str(e)}

def get_stock_price(ticker: str) -> str:
    """Get current stock price and basic info."""
    try:
        logger.info(f"Fetching stock price for: {ticker}")
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1d")

        if hist.empty:
            return f"Could not retrieve data for {ticker}"

        current_price = hist['Close'].iloc[-1]
        prev_close = info.get('previousClose', current_price)
        change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0

        result = {
            "ticker": ticker,
            "price": round(current_price, 2),
            "change_percent": round(change_pct, 2),
            "company": info.get('longName', ticker)
        }

        return json.dumps(result)
    except Exception as e:
        logger.error(f"Error in get_stock_price for {ticker}: {str(e)}")
        return f"Error: {str(e)}"

def compare_stocks(tickers: str) -> str:
    """Compare multiple stocks (comma-separated)."""
    try:
        logger.info(f"Comparing stocks: {tickers}")
        ticker_list = [t.strip().upper() for t in tickers.split(',')]
        comparison = []

        for ticker in ticker_list:
            stock = yf.Ticker(ticker)
            info = stock.info
            hist = stock.history(period="1d")

            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                prev_close = info.get('previousClose', current_price)
                change_pct = ((current_price - prev_close) / prev_close * 100) if prev_close else 0

                comparison.append({
                    "ticker": ticker,
                    "price": round(current_price, 2),
                    "change_percent": round(change_pct, 2)
                })

        return json.dumps(comparison)
    except Exception as e:
        logger.error(f"Error in compare_stocks: {str(e)}")
        return f"Error: {str(e)}"
