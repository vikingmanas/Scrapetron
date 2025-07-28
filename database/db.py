import sqlite3

def save_to_db(data):
    conn = sqlite3.connect("scraped_data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS items (title TEXT)")

    for row in data:
        c.execute("INSERT INTO items (title) VALUES (?)", (row["title"],))

    conn.commit()
    conn.close()
