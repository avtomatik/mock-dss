from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import routes_sign

app = FastAPI(
    title="Digital Signature Service",
    version="0.1.0",
    description="Toy digital signature service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_sign.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Digital Signature Service running."}
