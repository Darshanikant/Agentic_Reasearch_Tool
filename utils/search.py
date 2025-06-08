# utils/search.py

from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 5):
    """Search the web using DuckDuckGo and return a list of snippets."""
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "body": r.get("body"),
                "href": r.get("href")
            })
    return results
