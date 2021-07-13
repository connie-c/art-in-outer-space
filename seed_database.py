"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
from playlist import Videos
from projects import Projects
from artpieces import Artpieces

import crud 
import model
import server
import playlist
import projects
import artpieces

os.system("dropdb reviews")
os.system("createdb reviews")

model.connect_to_db(server.app)
model.db.create_all()


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
    # print(video['video_id'])

    db_video = crud.create_video(title, description, url, video_id)

# Create projects from Projects dictionary
projects_in_db = Projects

for project in Projects:

    project_title, artist_name, description, url, img, project_id = (
        project["project_title"],
        project["description"],
        project["artist_name"],
        project["url"],
        project["img"],
        project["project_id"]
    )
    print(project['project_id'])

    db_project = crud.create_project(project_title, description, artist_name, url, img, project_id)

# Create 10 users; each user will make 10 review rankings
for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password)

    for _ in range(10):
        random_video = choice(videos_in_db)
        ranking = randint(1, 10)

        crud.create_review(user, ranking, video_id)

# Create artpieces from Artpieces dictionary
artpieces_in_db = Artpieces

for artpiece in Artpieces:

    artpiece_id, name, price, image_url, color = (
        artpiece["artpiece_id"],
        artpiece["name"],
        artpiece["price"],
        artpiece["image_url"],
        artpiece["color"]
    )
    print(artpiece['artpiece_id'])

    db_project = crud.create_artpiece(artpiece_id, name, price, image_url, color)



#     video = Videos
#     print("success")
# return video
    # date = datetime.strptime(video["date"], "%Y-%m-%d")
    # db_video = crud.create_video(video)

    # db_movie = crud.create_video(title, description, date, creator, url)
    # videos_in_db.append(db_video)