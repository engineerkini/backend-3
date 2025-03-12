from fastapi import FastAPI
from app.routes import user, song

app = FastAPI()

app.include_router(user.router, prefix="/api")
app.include_router(song.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Spotify Backend"}
