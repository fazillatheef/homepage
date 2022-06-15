import sqlite3 as sql3
conn=sql3.connect("links.db")

sql_insert = """
INSERT INTO cards (
    card_name
) VALUES (
    :card_name
)
"""
for card in [{'card_name':'First'},{'card_name':'Second'}]:
    result = conn.execute(sql_insert,card)
    print(result.lastrowid,result.rowcount)
conn.commit()
conn.close()