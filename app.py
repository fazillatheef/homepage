from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

for env_var in ['SQLALCHEMY_DATABASE_URI']:
    if env_var in os.environ.keys():
        app.config[env_var] = os.environ[env_var]
    else:
        raise ValueError("Environment variables not setup!!")

db = SQLAlchemy(app)

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    links = db.relationship('Link', cascade='all, delete', lazy=True)


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

class Shortcut(db.Model):
    __tablename__ = 'shortcuts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)

@app.route('/edit')
def index_edit():
    groups = Group.query.all()
    return render_template('edit.html', groups=groups)

@app.route('/add_shortcut', methods=['POST','GET'])
def add_shortcut():
    if request.method == 'GET':
        return render_template('add_shortcut.html')
    elif request.method == 'POST':
        text = request.form['text']
        url = request.form['url']
        try:
            db.session.add(Shortcut(text=text, url=url))
            db.session.commit()
        except:
            db.session.rollback()
            raise        
        return render_template('edit.html')

@app.route('/create_group', methods=['POST'])
def create_group():
    name = request.form['name']
    group = Group(name=name)

    try:
        db.session.add(group)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect('/edit')

@app.route('/remove_group/<int:group_id>', methods=['POST'])
def remove_group(group_id):
    try:
        group = Group.query.get(group_id)
        db.session.delete(group)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect('/edit')

@app.route('/add_link/<int:group_id>', methods=['POST'])
def add_link(group_id):
    text = request.form['text']
    url = request.form['url']

    try:
        group = Group.query.get(group_id)
        link = Link(text=text, url=url)
        group.links.append(link)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect('/edit')

@app.route('/remove_link/<int:link_id>', methods=['POST'])
def remove_link(link_id):
    try:
        link = Link.query.get(link_id)
        db.session.delete(link)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect('/edit')

if __name__ == "__main__":
    app.run()