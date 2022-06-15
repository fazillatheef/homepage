import sqlite3 as sql3
conn=sql3.connect("links.db")

sql_insert = """
INSERT INTO links (
    card_id,
    link_text,
    link
) VALUES (
    :card_id,
    :link_text,
    :link
)
"""
for card in [{'card_id':1,'link_text':'Link1','link':'http://example.com'}\
            ,{'card_id':1,'link_text':'Link2','link':'http://free.com'}\
            ,{'card_id':1,'link_text':'Link3','link':'http://tree.com'}\
            ,{'card_id':2,'link_text':'Link1','link':'http://ginger.com'}\
            ,{'card_id':2,'link_text':'Link2','link':'http://juice.com'}\
            ]:
    result = conn.execute(sql_insert,card)
    print(result.lastrowid,result.rowcount)
conn.commit()
conn.close()