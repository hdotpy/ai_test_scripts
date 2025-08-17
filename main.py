# main.py (Fixed)
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from routes.test_generator import router as test_router

app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register routes
app.include_router(test_router)  # No prefix


@app.get("/")
def home():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/static/index.html")


@app.exception_handler(500)
async def handle_500(request: Request, exc):
    return Response(content=f"Server Error: {exc}", status_code=500)
