# api/index.py
# This file is the Vercel function entrypoint.
# Vercel looks for a top-level `app` (WSGI/ASGI) or `handler`.

# Import your FastAPI app from main.py
from main import app  # <-- make sure main.py defines `app = FastAPI()`
