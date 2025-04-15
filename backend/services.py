import requests

# Replace this with your actual key (consider storing in .env later)
API_KEY = "4d3b5b9978mshd8485a52b40c1bap157775jsnea1d370919e7"
BASE_URL = "https://yh-finance.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
}


def search_stock(query):
    """Search for a stock by name or symbol."""
    url = f"{BASE_URL}/auto-complete?q={query}&region=US"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def get_stock_summary(symbol):
    """Get stock summary data (price, stats, etc.)"""
    url = f"{BASE_URL}/stock/v2/get-summary?symbol={symbol}&region=US"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
