# services/scraper.py
from playwright.async_api import async_playwright


async def scrape_page(url: str) -> str:
    """
    Use Playwright Async API to load and return page HTML.
    This avoids blocking the asyncio loop.
    """
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, timeout=30000)
            await page.wait_for_load_state("networkidle")
            html = await page.content()
            await browser.close()
            return html
    except Exception as e:
        raise Exception(f"Failed to load page: {str(e)}")
