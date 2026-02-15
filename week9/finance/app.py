import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]

    # Get user's stocks
    rows = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, user_id)

    portfolio = []
    grand_total = 0

    for row in rows:
        stock = lookup(row["symbol"])
        if stock:
            total = row["total_shares"] * stock["price"]
            grand_total += total

            portfolio.append({
                "symbol": row["symbol"],
                "shares": row["total_shares"],
                "price": stock["price"],
                "total": total
            })

    # Get cash
    cash_row = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash_row[0]["cash"]

    grand_total += cash

    return render_template("index.html",
                           portfolio=portfolio,
                           cash=cash,
                           grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        # Get symbol and shares
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate symbol
        if not symbol:
            return apology("must provide symbol")

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        # Validate shares
        if not shares:
            return apology("must provide number of shares")
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("shares must be positive integer")
        except ValueError:
            return apology("shares must be positive integer")

        # Check cash
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]
        total_price = stock["price"] * shares
        if total_price > cash:
            return apology("can't afford")

        # Insert transaction
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol, shares, stock["price"])

        # Update cash
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_price, session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]

    # Query all transactions
    transactions = db.execute(
        "SELECT symbol, shares, price, datetime FROM transactions WHERE user_id = ? ORDER BY datetime DESC", user_id
    )

    return render_template("history.html", transactions=transactions)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide symbol")

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        return render_template("quoted.html", stock=stock)

    else:
        return render_template("quote.html")







@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Check username
        username = request.form.get("username")
        if not username:
            return apology("Must provide username")

        # Check password
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not password or not confirmation:
            return apology("Must provide password")

        if password != confirmation:
            return apology("passwords must match")

        # Hash password
        hash = generate_password_hash(password)

        # Insert into database
        try:
            user_id = db.execute(
                "INSERT INTO users (username, hash) VALUES(?, ?)",
                username, hash
            )

        except ValueError:
            return apology("username already exists")

        # Log user in
        session["user_id"] = user_id

        return redirect("/")


    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""


    user_id = session["user_id"]

    if request.method == "POST":
        # Get form data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate selection
        if not symbol:
            return apology("must select a stock")

        # Validate shares
        if not shares:
            return apology("must provide number of shares")
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("shares must be positive integer")
        except ValueError:
            return apology("shares must be positive integer")

        # Check how many shares user owns
        rows = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ?", user_id, symbol)
        owned = rows[0]["total_shares"]
        if not owned or shares > owned:
            return apology("not enough shares to sell")

        # Lookup current price
        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        # Record transaction (as negative shares)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   user_id, symbol, -shares, stock["price"])

                # Update cash
        total_sale = shares * stock["price"]
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sale, user_id)

        return redirect("/")

    else:
        # GET: show form with dropdown of stocks user owns
        stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", user_id)
        return render_template("sell.html", stocks=stocks)

@app.route("/change", methods=["GET", "POST"])
@login_required
def change():

    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Validate input
        if not old_password or not new_password or not confirmation:
            return apology("must fill all fields")

        if new_password != confirmation:
            return apology("passwords must match")

        # Get current user's hash
        rows = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])

        if not check_password_hash(rows[0]["hash"], old_password):
            return apology("invalid old password")

        # Update password
        new_hash = generate_password_hash(new_password)

        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, session["user_id"])

        return redirect("/")

    else:
        return render_template("change.html")

