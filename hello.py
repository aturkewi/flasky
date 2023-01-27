from datetime import datetime

from flask import Flask, request, make_response, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
  name = StringField('What is your name?', validators=[DataRequired()])
  submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5be49645039d258fb4024c971409c749'
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
