# Standard Lib
from numbers import Number
from re import search
# Flask Lib
from flask import g

# Return the column types of a table
def header_types(tbl_name):
    cur = g.db.cursor()
    cur.execute("PRAGMA TABLE_INFO (%s)" % (tbl_name))
    heads = cur.fetchall()
    cur.close()
    return [str(head[1]) for head in heads]

# Insert a row into a table given the values
def insert(tbl_name, values):
    try:
        cur = g.db.cursor()
        data_string = ""
        for value in values:
            if isinstance(value, Number) or bool(search("^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$", value)):
                data_string += str(value) + ","
            elif value == "datetime('now')" or value == "NULL":
                data_string += value + ","
            else:
                data_string += "'%s'," % value
        cur.execute("INSERT INTO %s VALUES (%s)" %
                    (tbl_name, data_string[:-1]))
        g.db.commit()
        cur.close()
        return True
    except:
        return False

# Get certain data from a table
def get(tbl_name, column, conditional=""):
    cur = g.db.cursor()
    cur.execute("SELECT %s FROM %s %s" % (column, tbl_name, conditional))
    values = cur.fetchall()
    cur.close()
    return [list(value) for value in values]
