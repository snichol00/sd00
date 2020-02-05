# Flask Lib
from flask import g
# User Modules
from .dbfunc import insert, get

# Create a post given the following parameters
def create_post(userid, author, title, content):
    try:
        insert("blogs", ["NULL", userid, author,
                         title, content, "datetime('now')"])
        blogid = get("blogs", "blogid", "WHERE title = '%s'" % title)[0][0]
        return blogid
    except:
        return False

# Update a post given the following parameters
def update_post(blogid, blogcontent, blogtitle):
    try:
        cur = g.db.cursor()
        cur.execute(
            "UPDATE blogs SET content = '%s', lastupdated = datetime('now'), title='%s' WHERE blogid = '%s'" % (
                blogcontent, blogtitle, blogid
            )
        )
        g.db.commit()
        cur.close()
        return True
    except:
        return False

# Update a user's settings given the field and new value
def update_user(username, field, newvalue):
    try:
        cur = g.db.cursor()
        cur.execute(
            "UPDATE users SET %s = '%s' WHERE username = '%s'" % (
                field,
                newvalue,
                username
            )
        )
        g.db.commit()
        cur.close()
        return "Operation Successful"
    except:
        return "Error With Update"

# Delete a post given the blog id.
def delete_post(blogid):
    try:
        cur = g.db.cursor()
        cur.execute("DELETE FROM blogs WHERE blogid = '%s'" % blogid)
        g.db.commit()
        cur.close()
        return True
    except:
        return False
