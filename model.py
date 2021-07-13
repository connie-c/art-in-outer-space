"""Models for art-in-outer-space web app, including Dear Moon YouTube videos, and reviews section."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # reviews = a list of Review objects

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Video(db.Model):
    """A video."""

    __tablename__ = "videos"

    title = db.Column(db.String)
    description = db.Column(db.Text)
    # date = db.Column(db.DateTime)
    # creator = db.Column(db.String)
    url = db.Column(db.String)
    video_id = db.Column(db.String, primary_key=True)
    # video_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # reviews = a list of Review objects

    def __repr__(self):
        # return f"<Video video_id={self.video_id} url={self.url}>"
        return f"<Video video_id={self.video_id} title={self.title} description={self.description} url={self.url}>"


class Review(db.Model):
    """A video review."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # review_comment = db.Column(db.String)
    ranking = db.Column(db.Integer)
    video_id = db.Column(db.String, db.ForeignKey("videos.video_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    video = db.relationship("Video", backref="reviews")
    user = db.relationship("User", backref="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} ranking={self.ranking}>"

class Project(db.Model):
    """An art project."""

    __tablename__ = "projects"

    project_title = db.Column(db.String)
    description = db.Column(db.Text)
    # date = db.Column(db.DateTime)
    artist_name = db.Column(db.String)
    url = db.Column(db.String)
    img = db.Column(db.String)
    project_id = db.Column(db.String, primary_key=True)

    # comments = a list of Comment objects

    def __repr__(self):
        return f"<Project project_id={self.project_id} project_title={self.project_title} description={self.description} artist_name={self.artist_name} url={self.url} img={self.img}>"

class Comment(db.Model):
    """An art project comment."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    comment = db.Column(db.String)
    project_id = db.Column(db.String, db.ForeignKey("projects.project_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    project = db.relationship("Project", backref="comments")
    user = db.relationship("User", backref="comments")

    def __repr__(self):
        return f"<Comment comment_id={self.comment_id} comment={self.comment}>"

class Artpiece(db.Model):
    """Art piece"""

    __tablename__ = 'artpieces'

    artpiece_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)

    # artpiece_type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))

    # artpiece_type = db.relationship('ArtpieceType', backref='artpieces')

    def __repr__(self):
        return f"<Artpiece artpiece_id={self.artpiece_id} name={self.name} price={self.price} image_url={self.image_url} color={self.color} >"
    
    def to_dict(self):
        return {'artpiece_id': self.artpiece_id,
                'name': self.name,
                'price': self.price,
                'image_url': self.image_url,
                'color': self.color
                }


# class ArtpieceType(db.Model):
#     """Type of art piece."""

#     __tablename__ = 'types'

#     type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     name = db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return f'<ArtpieceType name={self.name}>'

    # def to_dict(self):
    #     return {'type_id': self.type_id,
    #             'name': self.name}


def connect_to_db(flask_app, db_uri="postgresql:///reviews", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
