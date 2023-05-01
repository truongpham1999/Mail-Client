import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

# Make sure API key is set
#if not os.environ.get("API_KEY"):
#   raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def inbox():
    """Show all the emails receiverd"""
    if request.method == "GET":
        userid = session["user_id"]
        recipient = db.execute("SELECT username FROM users WHERE id = ?", userid)[0]["username"]

        # get all the  received emails by other users
        emails = db.execute ("SELECT * FROM emails WHERE recipient = ?", recipient)

        return render_template("mail_received.html", emails=emails)


@app.route("/compose", methods=["GET", "POST"])
@login_required
def compose():
    """write an email to someone"""
    if request.method == "GET":
        userid = session["user_id"]
        sender = db.execute("SELECT username FROM users WHERE id = ?", userid)[0]["username"]
        return render_template("compose.html", sender=sender)
    else:
        sender = request.form.get("sender")
        recipient = request.form.get("recipient")
        subject = request.form.get("subject")
        body = request.form.get("body")

        if not sender or not recipient or not subject or not body:
            return apology("Please fill all the fields")

        # return apology if receiver doesn't exist
        if not db.execute("SELECT * FROM users WHERE username = ?", recipient):
            return apology("Receiver doesn't exist")

        # insert email into database
        db.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)", sender, recipient, subject, body)

        # redirect user to sent page
        return redirect("/sent")


@app.route("/sent")
@login_required
def sent():
    """Show sent emails"""
    if request.method == "GET":
        userid = session["user_id"]
        sender = db.execute("SELECT username FROM users WHERE id = ?", userid)[0]["username"]

        # get all the emails sent by the user
        emails = db.execute ("SELECT * FROM emails WHERE sender = ?", sender)

        return render_template("sent.html", emails=emails)




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/received_email_viewing", methods=["POST"])
@login_required
def received_viewing():
    """View received email details."""
    if request.method == "POST":
        email_id = request.form.get("email_id")
        email_details = db.execute("SELECT * FROM emails WHERE id = ?", email_id)[0]
        return render_template("received_email_viewing.html", email_details=email_details)


@app.route("/sent_email_viewing", methods=["POST"])
@login_required
def sent_viewing():
    """View sent email details."""
    if request.method == "POST":
        email_id = request.form.get("email_id")
        email_details = db.execute("SELECT * FROM emails WHERE id = ?", email_id)[0]
        return render_template("sent_email_viewing.html", email_details=email_details)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        user = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not user or not password or not confirmation:
            return apology("Please fill all the fields")
        elif password != confirmation:
            return apology("Password and confirmation must be the same")
        elif len(password) < 8:
            return apology("Password must be at least 8 characters long")
        elif user.isupper():
            return apology("Username must be lowercase")
        elif db.execute("SELECT * FROM users WHERE username = ?", user):
            return apology("Username already exists")

        #generate hash password
        hash = generate_password_hash(password)

        #insert user into database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", user, hash)

        #remember user
        session["user_id"] = db.execute("SELECT id FROM users WHERE username = ?", user)[0]["id"]

        #redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/reply", methods=["POST"])
@login_required
def reply():
    """Reply the email on email detail view"""
    if request.method == "POST":
        email_id = request.form.get("email_id")
        email_details = db.execute("SELECT * FROM emails WHERE id = ?", email_id)[0]
        return render_template("reply.html", email_details=email_details)


@app.route("/send_reply", methods=["POST"])
@login_required
def send_reply():
    """Send a reply to an email"""
    sender = request.form.get("sender")
    recipient = request.form.get("recipient")
    subject = request.form.get("subject")
    body = request.form.get("body")

    if not sender or not recipient or not subject or not body:
        return apology("Please fill all the fields")

    # return apology if receiver doesn't exist
    if not db.execute("SELECT * FROM users WHERE username = ?", recipient):
        return apology("Receiver doesn't exist")

    # insert email into database
    db.execute("INSERT INTO emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)", sender, recipient, subject, body)

    # redirect user to sent page
    return redirect("/sent")
