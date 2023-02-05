from datetime import datetime
import os

from flask import Flask, request, make_response, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

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

migrate = Migrate(app, db)

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)
  # The lazy='dynamic' here makes it so that when calling `users`, a query is returned instead of an EXECUTED query. This makes querying more explicit and gives the dev the change to filter, order...
  users = db.relationship('User', backref='role', lazy='dynamic')
  
  def __repr__(self):
    return '<Role %r>' % self.name
  
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, index=True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  
  def __repr__(self):
    return '<User %r>' % self.username


bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  form = NameForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.name.data).first()
    if user is None:
      user = User(username=form.name.data)
      db.session.add(user)
      db.session.commit()
      session['known'] = False
    else:
      session['known'] = True
    session['name'] = form.name.data
    form.name.data = ''
    return redirect(url_for('index'))
  return render_template('index.html',
    form=form, name=session.get('name'),
    known=session.get('known', False))

@app.route('/users/<name>')
def user(name):
  return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500

# Auto-loads with shell
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
  
# This was needed before the `flask` command could be used to run the app
# if __name__ == '__main__':
#     app.run()
