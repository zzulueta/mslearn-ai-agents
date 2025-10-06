import json
from typing import Any, Callable, Set

# For web scraping
import requests
from bs4 import BeautifulSoup

# Function to scrape info from a URL
def scrape_url_info(url: str) -> str:
    """
    Scrapes all visible text content from the given URL.
    Returns a JSON string with the URL and the extracted text or error message.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove script and style elements
        for tag in soup(['script', 'style', 'noscript']):
            tag.decompose()
        # Get visible text
        text = soup.get_text(separator=' ', strip=True)
        # Optionally, limit the length to avoid huge outputs
        max_length = 5000
        if len(text) > max_length:
            text = text[:max_length] + '... [truncated]'
        result = {
            'url': url,
            'text': text
        }
        return json.dumps(result)
    except Exception as e:
        return json.dumps({'error': str(e), 'url': url})


# Define a set of callable functions
user_functions: Set[Callable[..., Any]] = {
    scrape_url_info
}


