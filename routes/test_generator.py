# routes/test_generator.py
from fastapi import APIRouter, Request
from services.scraper import scrape_page  # Still imports same function
from services.ai_generator import generate_test_script
from utils.helpers import clean_html
from config.settings import MAX_HTML_LENGTH

router = APIRouter()


@router.post("/generate")
async def generate_test(request: Request):
    """
    API endpoint: Accepts a URL, scrapes the page,
    uses AI to generate a test, and returns downloadable code.
    """
    data = await request.json()
    url = data.get("url")

    if not url:
        return {"error": "URL is required"}

    if not url.startswith("http"):
        url = "https://" + url

    try:
        # Step 1: Scrape the page (now async!)
        html = await scrape_page(url)  # ← Note: await here!

        # Step 2: Clean HTML
        cleaned_html = clean_html(html)

        # Step 3: Generate test script with AI
        code = generate_test_script(cleaned_html, url)

        # Return as downloadable response
        return {
            "code": code,
            "filename": "test_auto.py"
        }

    except Exception as e:
        return {"error": str(e)}
