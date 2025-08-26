from fastapi import FastAPI
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from routes.test_generator import router as test_router

app = FastAPI()

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Register routes
app.include_router(test_router)


@app.get("/")
def home():
    return RedirectResponse(url="/static/index.html")


@app.exception_handler(500)
async def handle_500(request: Request, exc: Exception):
    return Response(content=f"Server Error: {exc}", status_code=500)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
