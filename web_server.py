from flask import Flask
from flask import render_template
from db.link_database import linkdb

app = Flask(__name__)
cards = [{"title":"Main","content":[{"link":"Link1","address":"LinkAddress1"},{"link":"Link2","address":"LinkAddress2"}]},{"title":"Sub","content":[{"link":"Link3","address":"LinkAddress3"},{"link":"Link4","address":"LinkAddress4"}]}]

@app.route("/")
def main_page():
    link_data = linkdb("./db/links.db")
    cards = link_data.read_cards_links()
    return render_template('index.html',cards=cards)

@app.route("/edit")
def edit_page():
    return render_template('edit.html',cards=cards,edit=True)

if __name__ == '__main__':
    app.run(host='localhost',port=2020,debug=True)