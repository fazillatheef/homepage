import sqlite3 as sql3

class linkdb:
    def __init__(self,path):
        self.conn = sql3.connect(path)
        self.conn.row_factory = sql3.Row
    def read_cards_links(self):
        # returns a list with cards and links
        # [
        #   {
        #       "title"  :<card name>
        #       "content":[
        #                   {
        #                       "link"      :<Link Name>
        #                       "address"   :<Url>
        #                   },
        #                   ... other links
        #                 ]
        #   },
        #   ... other cards
        # ]
        card_list = []
        card_cursor = self.conn.cursor()
        link_cursor = self.conn.cursor()
        cards = card_cursor.execute('SELECT id,card_name from cards')
        while True:
            card_result = cards.fetchone()
            each_card = {}
            if not card_result:
                break
            each_card["title"]=card_result["card_name"]
            each_card["content"] = []
            links = link_cursor.execute(f'SELECT link_text,link from links where card_id=:card_id',{"card_id" : card_result["id"]})
            while True:
                link_result = links.fetchone()
                each_link = {}
                if not link_result:
                    break
                each_link["link"]= link_result["link_text"]
                each_link["address"]= link_result["link"]
                each_card["content"].append(each_link)
            card_list.append(each_card)

        card_cursor.close()
        link_cursor.close()
        return card_list
            
    def __del__(self):
        self.conn.close() 