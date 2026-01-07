from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router import router

app = FastAPI(
    title="AI-Wiki api",
    description="api for AI-Wiki",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "AI Wiki API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
