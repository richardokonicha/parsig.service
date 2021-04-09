#!/usr/bin/env python3

from fastapi import FastAPI
from api.routes import router as NoteRouter


app = FastAPI(
    title="Parsig service backend",
    description="The backend api for parsig service",
    version="0.1.0",
    docs_url='/docs',
    openapi_url='/docs/openapi.json',
    redoc_url='/redocs'
)

app.include_router(NoteRouter, prefix="/note")

@app.get('/api/hello')
async def hello():
    return {'message': 'Hello world!'}

@app.get('/')
async def hello():
    return {"message":"you won smoke you gon find me in Gotham"}