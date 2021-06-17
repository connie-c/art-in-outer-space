"""CRUD operations."""

from model import db, User, Review, Video, connect_to_db
from playlist import Videos  # rename to youtube_videos_list

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


# def create_videos(title, description, url, video_id):
#     """Create and return a new YouTube video, and add to database"""

#     for youtube_video in Videos:
#     # print(video)
#         database_video = Video(
#         title=youtube_video['title'],
#         description=description,
#         url=url,
#         video_id=video_id
#     )
#         db.session.add(video)
#         db.session.commit()

#     return video

def create_video(title, description, url, video_id):
    """Create and return a new YouTube video, and add to database"""

    video = Video(
        title=title,
        description=description,
        url=url,
        video_id=video_id
    )
    db.session.add(video)
    db.session.commit()

    return video


# def get_videos_from_youtube():
#     """Return all videos."""

#     return Videos

def get_video_by_id(video_id):
    """Return a video by primary key."""
    print(video_id)
    return get_video_by_id(video_id)


def get_videos_from_database():
    """Return all videos."""
    print('get_videos_from_database')
    return Video.query.all()


def get_video_by_id(video_id):
    """Return a video by primary key."""

    return Video.query.get(video_id)


def create_review(user, ranking, video_id):
    """Create and return a new ranking."""

    ranking = Review(user=user, ranking=ranking, video_id=video_id)

    db.session.add(ranking)
    db.session.commit()

    return ranking


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
