"""CRUD operations."""

from model import db, User, Review, Video, Project, Comment, Artpiece, connect_to_db
from playlist import Videos  # rename to youtube_videos_list
from projects import Projects
from artpieces import Artpieces

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


def create_review(user, video, ranking):
    """Create a new ranking and add to the database."""

    ranking = Review(user=user, video=video, ranking=ranking)

    db.session.add(ranking)
    db.session.commit()

    return ranking


"""get_inspired art project portion"""

def create_project(project_title, artist_name, description, url, img, project_id):
    """Create and return a new art project, and add to database"""

    project = Project(
        project_title=project_title,
        artist_name=artist_name,
        description=description,
        url=url,
        img=img,
        project_id=project_id
    )
    db.session.add(project)
    db.session.commit()

    return project


# def get_project_by_id(project_id):
#     """Return a project by primary key."""
#     print(project_id)
#     return get_project_by_id(project_id)


def get_projects_from_database():
    """Return all projects from database."""
    print('get_projects_from_database')
    return Project.query.all()


def get_project_by_id(project_id):
    """Return a project by primary key."""

    return Project.query.get(project_id)


def create_comment(user, project, comment):
    """Create and return a new comment."""

    comment = Comment(user=user, project=project, comment=comment)

    db.session.add(comment)
    db.session.commit()

    return comment


"""get_funded art piece portion"""

def create_artpiece(artpiece_id, name, price, image_url, color):
    """Create and return a new art piece, and add to database"""

    artpiece = Artpiece(
        artpiece_id=artpiece_id,
        name=name,
        price=price,
        image_url=image_url,
        color=color
    )
    db.session.add(artpiece)
    db.session.commit()

    return artpiece


def get_artpieces_from_database():
    """Return all art pieces from database."""
    print('get_artpieces_from_database')
    return Artpiece.query.all()


def get_artpiece_by_id(artpiece_id):
    """Return a artpiece by primary key."""

    return Artpiece.query.get(artpiece_id)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
