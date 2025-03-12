from database import SessionLocal
from models.user import User
from models.song import Song

def add_data():
    session = SessionLocal()
    
    user = User(name="Alice", email="alice@example.com")
    session.add(user)
    session.commit()

    song = Song(title="Shape of You", artist="Ed Sheeran", user_id=user.id)
    session.add(song)
    session.commit()

    print(f"User added: {user.name}")
    print(f"Song added: {song.title} by {song.artist}")

    session.close()

add_data()
