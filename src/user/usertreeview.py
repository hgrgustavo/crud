from database import Database


def fetch():
    database = Database()

    if database.cursor.execute("SELECT * FROM user"):
        return database.cursor.fetchall()

    database.connection.close()


def populate_treeview(treeview):
    # data = fetch_user()

    for row in fetch():
        treeview.insert("", "end", values=row)




