# Standard Lib
from sqlite3 import connect
# Flask Lib
from flask import current_app, g

# Initialize a database connection
def conn():
    if "db" not in g:
        g.db = connect(current_app.config["DATABASE"])

# Close an existing database connection
def close():
    db = getattr(g, "db", None)
    if db is not None:
        db.close()
