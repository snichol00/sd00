# Standard Lib
from hashlib import sha256
# Flask Lib
from flask import current_app, g

# User Modules
from .dbfunc import insert, get
from .edit import update_user

# Hash the password using SHA-256 algorithm
def get_hash(password):
    return sha256((current_app.config["SALT"] + password).encode()).hexdigest()

# Authenticates the user given a username and password with the hashed password
def auth(username, password):
    try:
        hashpassword = get("users", "hashpassword",
                           "WHERE username = '%s'" % username)[0][0]
        if get_hash(password) == hashpassword:
            return True
    except:
        return False

# Registers the user given a username and a password and the displayname is optional
def register(username, password, displayname):
    if not auth(username, password):
        if not displayname:
            displayname = username
        insert("users", ["NULL", username, get_hash(password), displayname])
    return True

# Updates the password of the current user
def update_auth(username, currentpassword, newpassword):
    try:
        assert auth(username, currentpassword), "Wrong Password"
        return update_user(username, "hashpassword", get_hash(newpassword))
    except AssertionError as ae:
        return str(ae.args[0])