"""

Personal Expense Tracker — Flask + SQLite

=========================================



A simple app to track money coming in (income) and going out (expenses).



Pages / routes

--------------

GET  /              → dashboard: current balance + totals

GET  /add/          → show the "add transaction" form

POST /add/          → validate the form, save it, go back to the dashboard

GET  /history/      → list every transaction



All data is stored in an SQLite database file: data/expenses.db

"""

import os

from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import SQLAlchemyError

# --------------------------------------------------------------------------- #

# 1. App & database setup

# --------------------------------------------------------------------------- #

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "expenses.db")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --------------------------------------------------------------------------- #

# 2. The database table (our "schema")

# --------------------------------------------------------------------------- #

class Transaction(db.Model):
    """One row = one thing you added (an income or an expense)."""

    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)

    type = db.Column(db.String(10), nullable=False)  # "income" or "expense"

    category = db.Column(db.String(80), nullable=False)  # e.g. "Food", "Salary"

    amount = db.Column(db.Float, nullable=False)  # always stored positive

    description = db.Column(db.String(200), nullable=True)  # optional note


def init_db():
    """Create the database tables if they don't exist yet."""

    with app.app_context():
        db.create_all()


# --------------------------------------------------------------------------- #

# 3. A small helper to add up the totals

# --------------------------------------------------------------------------- #

def compute_totals():
    """Return (total_income, total_expenses, balance)."""

    income = db.session.query(

        db.func.coalesce(db.func.sum(Transaction.amount), 0)

    ).filter(Transaction.type == "income").scalar()

    expenses = db.session.query(

        db.func.coalesce(db.func.sum(Transaction.amount), 0)

    ).filter(Transaction.type == "expense").scalar()

    balance = income - expenses

    return income, expenses, balance


# --------------------------------------------------------------------------- #

# 4. Validation helper

# --------------------------------------------------------------------------- #

def validate_form(form):
    """

    Check the submitted form. If everything is good, return a tidy tuple.

    If something is wrong, raise ValueError with a friendly message.

    """

    tx_type = form.get("type", "")

    if tx_type not in ("income", "expense"):
        raise ValueError("Please choose income or expense.")

    category = (form.get("category") or "").strip()

    if not category:
        raise ValueError("Category is required.")

    # float() throws an error if the text isn't a number.

    amount = float(form.get("amount", ""))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    description = (form.get("description") or "").strip()

    return tx_type, category, amount, description


# --------------------------------------------------------------------------- #

# 5. Routes (the pages)

# --------------------------------------------------------------------------- #

@app.route("/")
def index():
    try:

        income, expenses, balance = compute_totals()

    except SQLAlchemyError:

        db.session.rollback()

        return render_template("error.html", code=500,

                               message="Database error loading the dashboard."), 500

    return render_template("index.html",

                           income=income, expenses=expenses, balance=balance)


@app.route("/add/", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        # First: is the data valid?

        try:

            tx_type, category, amount, description = validate_form(request.form)

        except ValueError as exc:

            return render_template("add.html", error=str(exc),

                                   form=request.form), 400

        # Second: try to save it.

        try:

            db.session.add(Transaction(

                type=tx_type,

                category=category,

                amount=amount,

                description=description,

            ))

            db.session.commit()

        except SQLAlchemyError:

            db.session.rollback()

            return render_template("add.html",

                                   error="A database error occurred. Please try again.",

                                   form=request.form), 500

        return redirect(url_for("index"))

    # If it's a GET request, just show the empty form.

    return render_template("add.html")


@app.route("/history/")
def history():
    try:

        rows = Transaction.query.order_by(Transaction.id.desc()).all()

    except SQLAlchemyError:

        db.session.rollback()

        return render_template("error.html", code=500,

                               message="Database error loading history."), 500

    return render_template("history.html", records=rows)


# --------------------------------------------------------------------------- #

# 6. Error pages

# --------------------------------------------------------------------------- #

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", code=404,

                           message="Page not found."), 404


@app.errorhandler(500)
def server_error(e):
    message = getattr(e, "description", "Internal server error.")

    return render_template("error.html", code=500, message=message), 500


# --------------------------------------------------------------------------- #

# 7. Start the app

# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    init_db()  # make sure the tables exist

    app.run(debug=True)
