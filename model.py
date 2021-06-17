"""Models for art-in-outer-space app, reviews section."""

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
    review_comment = db.Column(db.String)
    ranking = db.Column(db.Integer)
    video_id = db.Column(db.String, db.ForeignKey("videos.video_id"))
    # video_id = db.Column(db.Integer, db.ForeignKey("videos.video_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    video = db.relationship("Video", backref="reviews")
    user = db.relationship("User", backref="reviews")

    def __repr__(self):
        return f"<Review review_id={self.review_id} ranking={self.ranking}>"


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
