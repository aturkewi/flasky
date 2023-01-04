from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  user_agent = request.headers.get('User-Agent')
  return '<h1>Hello World! You are viewing this on {}</h1>'.format(user_agent)

@app.route('/users/<name>')
def user(name):
  return '<h1>Hello, {}!!!</h1>'.format(name)

# This was needed before the `flask` command could be used to run the app
# if __name__ == '__main__':
#     app.run()
