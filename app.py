from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    links = db.relationship('Link', backref='group', lazy=True)


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    groups = Group.query.all()
    return render_template('index.html', groups=groups)

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

    return redirect('/')

@app.route('/remove_group/<int:group_id>', methods=['POST'])
def remove_group(group_id):
    try:
        group = Group.query.get(group_id)
        db.session.delete(group)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect('/')

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

    return redirect('/')
@app.route('/remove_link/<int:link_id>', methods=['POST'])
def remove_link(link_id):
    try:
        link = Link.query.get(link_id)
        link.group.links.remove(link)
        db.session.delete(link)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    return redirect('/')
