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

### Request Obj

https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html#ch02_request_object

### Response Obj

https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html#ch02_response_object

### Jinja templates

Uses filters instead of python: `{{name | capitalize}}`
**Question: Why a special filter here? Why not use `.capitalize()`?**

If/else in Jinja:
```
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
```

For in jinja:
```
{% for comment in comments %}
    <li>{{ comment }}</li>
{% endfor %}
```

>Note the need for explicit `end`s in Jinja!

Ability to extend other templates (e.g. like a base template): `{% extends "bootstrap/base.html" %}`

