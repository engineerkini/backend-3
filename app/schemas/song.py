from pydantic import BaseModel

class SongCreate(BaseModel):
    title: str
    artist: str
    user_id: int

class SongResponse(SongCreate):
    id: int

    class Config:
        orm_mode = True
