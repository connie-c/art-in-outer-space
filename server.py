"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
import playlist

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/get_connected")
def all_videos():
    """View all videos."""

    videos = crud.get_videos_from_database()

    return render_template("get_connected.html", videos=videos)


@app.route("/get_connected/<video_id>")
def show_video(video_id):
    """Show details on a particular video."""

    video = crud.get_video_by_id(video_id)

    return render_template("video_details.html", video=video)

# @app.route("/get_inspired")
# def all_projects():
#     """View all art in outer space projects."""

#     projects = crud.get_projects()

#     return render_template("get_inspired.html", projects=projects)


# @app.route("/get_projects/<project_id>")
# def show_project(project_id):
#     """Show details on a particular project."""

#     video = crud.get_project_by_id(project_id)

#     return render_template("project_details.html", project=project)

# @app.route("/users")
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in.")

    return redirect("/")


# @app.route("/users/<user_id>")
# def show_user(user_id):
#     """Show details on a particular user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template("user_details.html", user=user)


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

@app.route("/get_connected/<video_id>/reviews", methods=["POST"])
# @app.route("/get_connected", methods=["POST"])
def create_review_view(video_id):
    """Create a new review for video."""

    logged_in_email = session.get("user_email")
    review_ranking = request.form.get("review")

    if logged_in_email is None:
        flash("You must log in to review a video.")
    elif not review_ranking:
        flash("Error: you didn't select a ranking for your review.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        video = crud.get_video_by_id(video_id)

        crud.create_review(user, video, int(review_ranking))

        flash(f"You ranked this video {review_ranking} out of 10.")

    return "Success"
    # return redirect(f"/get_connected/{video_id}")
    # return redirect(f"/get_connected")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
