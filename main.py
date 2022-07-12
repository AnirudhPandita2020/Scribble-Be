from fastapi import FastAPI

app = FastAPI(
    title="Scribble FastAPI",
    description="Multiplayer Draw and Guess game",
    version="1.0",
    contact={
        "name": "Anirudh Pandita",
        "url": "https://www.linkedin.com/in/anirudh-pandita-a0b532200/",
        "email": "kppkanu@gmail.com",
    }
)


@app.get("/", tags=["Main"])
async def main():
    return "Version 1.0.Will begin work shortly"
