# Flasky

Following along with [O'Reilly Flask book](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch01.html#idm140583871764176)

## Getting started

- Activate venv: `source venv/bin/activate`
  - To stop using venv, use `deactivate`
- `pip install flask` (This will need to be moved to a requirements eventually?)
- `bin/run` to start the app on localhost:5000

## Flask Notes

### Contexts

[4 contexts](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html#ch02_context_globals)

- `current_app`
- `g`
- `request`
- `session`

### Routes

Can create routes with decorators:
```python
@app.route('/')
def index():
```

Can view routes from a shell with `app.url_map`
