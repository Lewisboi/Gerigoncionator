from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from gerigoncionator import Gerigoncionator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GerigoncifyRequest(BaseModel):
    text: str


@app.post("/gerigoncify")
def gerigoncify(gerigoncify_request: GerigoncifyRequest):
    text = gerigoncify_request.text
    gerigoncified = Gerigoncionator().gerigoncify(text)
    return {"gerigoncified": gerigoncified}
