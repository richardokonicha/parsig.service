from fastapi import FastAPI
from server.routes import router as NoteRouter

app = FastAPI()

app.include_router(NoteRouter, prefix="/note")

@app.get("/", tags=["Root"])
def create_tg_session():
    return{
        "message":"you won smoke you gon find me in Gotham"
    }

