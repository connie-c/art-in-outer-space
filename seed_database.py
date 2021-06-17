"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
from playlist import Videos

import crud 
import model
import server
import playlist

os.system("dropdb reviews")
os.system("createdb reviews")

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
# with open("data/videos.json") as f:
#     video_data = json.loads(f.read())


# Create videos from YouTube API
videos_in_db = Videos

for video in Videos:

    title, description, url, video_id = (
        video["title"],
        video["description"],
        # video["creator"],
        # video["date"],
        video["url"],
        video["video_id"]
    )
    print(video['video_id'])

    db_video = crud.create_video(title, description, url, video_id)


#     video = Videos
#     print("success")
# return video
    # date = datetime.strptime(video["date"], "%Y-%m-%d")
    # db_video = crud.create_video(video)

    # db_movie = crud.create_video(title, description, date, creator, url)
    # videos_in_db.append(db_video)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password)

    for _ in range(10):
        random_video = choice(videos_in_db)
        ranking = randint(1, 10)

        crud.create_review(user, ranking, video_id)