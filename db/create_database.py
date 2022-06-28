import sqlite3 as sql3
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("--delete","-d",action="store_true",default=False)
args = argparser.parse_args()

conn = sql3.connect("links.db")

if args.delete:
    conn.execute("""
    DROP TABLE cards;
    """)  

    conn.execute("""
    DROP TABLE links;
    """) 


    conn.execute("""
    DROP TABLE images;
    """) 

    conn.execute("""
    DROP TABLE shortcuts;
    """)   

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