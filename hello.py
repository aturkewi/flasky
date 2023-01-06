from flask import Flask, request, make_response, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
  user_agent = request.headers.get('User-Agent')
  response = make_response('<h1>I got a cookie</h1>'.format(user_agent))
  response.set_cookie('answer', '42')
  return response

@app.route('/users/<name>')
def user(name):
  return render_template('user.html', name=name)

# This was needed before the `flask` command could be used to run the app
# if __name__ == '__main__':
#     app.run()
