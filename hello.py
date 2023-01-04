from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/users/<name>')
def user(name):
  return '<h1>Hello, {}</h1>'.format(name)

# This was needed before the `flask` command could be used to run the app
# if __name__ == '__main__':
#     app.run()
