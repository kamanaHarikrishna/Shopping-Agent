import requests

def search_product_link(query, serpapi_key):
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google",
        "num": 1
    }
    r = requests.get("https://serpapi.com/search", params=params)
    results = r.json()
    try:
        return results["organic_results"][0]["link"]
    except:
        return "🔗 No link found"
