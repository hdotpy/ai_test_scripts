# services/ai_generator.py
import requests
from config.settings import AI_MODEL, OLLAMA_URL


def generate_test_script(html: str, url: str) -> str:
    """
    Calls the local AI model (via Ollama) to generate a test script.
    """
    prompt = f"""
You are a senior test automation engineer.

Analyze this webpage: {url}

HTML Content:
{html}

Your Task:
1. Identify the main purpose (e.g., login).
2. List all interactive elements (inputs, buttons).
3. Suggest 3 test cases: valid, invalid, and edge case.
4. Generate a complete Python Playwright test using unittest.

Rules:
- Use sync_playwright (synchronous mode)
- Include setUp() and tearDown()
- Add meaningful assertions (e.g., check URL, text)
- Use proper waits (e.g., wait_for_load_state)
- Output ONLY Python code inside a markdown block
- Do not add explanations

Return only:
```python
# your generated code here
"""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": AI_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        content = result["response"]

        if "```python" in content:
            code = content.split("```python")[1].split("```")[0]
        else:
            code = content

        return code.strip()

    except requests.ConnectionError:
        raise Exception("❌ Ollama not running. Run: ollama serve")
    except Exception as e:
        raise Exception(f"❌ AI generation failed: {str(e)}")
