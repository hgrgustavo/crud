from database import Database


def fetch():
    database = Database()

    if database.cursor.execute("SELECT * FROM client"):
        return database.cursor.fetchall()

    database.connection.close()


def populate_treeview(treeview):
    # data = fetch()

    for row in fetch():
        treeview.insert("", "end", values=row)