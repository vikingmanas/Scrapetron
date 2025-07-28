import sqlite3
import csv

def export_to_csv(filename="output.csv"):
    conn = sqlite3.connect("scraped_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    rows = c.fetchall()

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Title"])
        writer.writerows(rows)

    conn.close()
