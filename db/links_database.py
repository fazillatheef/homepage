import sqlite3 as sql3
conn = sql3.connect("links.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS  cards (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    card_name text)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS links (
    card_id INTEGER,
    link_text  text,
    link text,
    FOREIGN KEY(card_id) REFERENCES cards(id)
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS images (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    path text
)
""")
conn.execute("""
CREATE TABLE IF NOT EXISTS shortcuts (
    shortcut_name text,
    image_id  INTEGER,
    shortcut_link text,
    FOREIGN KEY(image_id) REFERENCES images(id))
""")

conn.close()