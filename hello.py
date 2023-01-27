from datetime import datetime
import os

from flask import Flask, request, make_response, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

class NameForm(FlaskForm):
  name = StringField('What is your name?', validators=[DataRequired()])
  submit = SubmitField('Submit')
  
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '5be49645039d258fb4024c971409c749'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://avi:@localhost:5432/flasky'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

db = SQLAlchemy(app)

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)
  users = db.relationship('User', backref='role')
  
  def __repr__(self):
    return '<Role %r>' % self.name
  
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, index=True)
  role = db.Column(db.Integer, db.ForeignKey('roles.id'))
  
  def __repr__(self):
    return '<User %r>' % self.username


bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  # user_agent = request.headers.get('User-Agent')
  # response = make_response('<h1>I got a cookie</h1>'.format(user_agent))
  # response.set_cookie('answer', '42')
  # return response
  # print(datetime.utcnow())
  name = None
  form = NameForm()
  if form.validate_on_submit():
    old_name = session.get('name')
    if old_name is not None and old_name != form.name.data:
      flash('Looks like you changed your name!')
    session['name'] = form.name.data
    return redirect(url_for('index'))
  return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))

@app.route('/users/<name>')
def user(name):
  return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500
  
# This was needed before the `flask` command could be used to run the app
# if __name__ == '__main__':
#     app.run()
