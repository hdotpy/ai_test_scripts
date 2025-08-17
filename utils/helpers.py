# utils/helpers.py
from bs4 import BeautifulSoup
from config.settings import MAX_HTML_LENGTH  # ✅ Import it here!


def clean_html(html: str) -> str:
    """
    Remove scripts, styles, and unnecessary tags from HTML.
    Returns cleaned body content, limited to MAX_HTML_LENGTH.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    return str(soup.body or soup)[:MAX_HTML_LENGTH]
