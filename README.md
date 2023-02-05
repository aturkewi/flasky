# Flasky

Following along with [O'Reilly Flask book](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch01.html#idm140583871764176)

## Getting started

- Ensure dotenv is installed
- `pip install -r requirements.txt`
- Open a DB editor and manually create `flasky` DB.
- `bin/shell` to get an active shell. From the shell, run:
    - `from hello import db`
    - `db.create_all()`
    - These commands will create the DB
- `bin/run` to start the app on localhost:5000

### Debugging

`bin/shell` to get an active shell.

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

## Database

- `flask db migrate` to create migration
- `flask db upgrade` to run migration
- `flask db downgrade` to rollback

### Modify

```python
from hello import Role, User
# Create obj in memory
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)

# Stage for commit
# Can be added individually with `.add()` instead of `.add_all()`
# Add and add_all also perform update actions.
db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])

# Write to DB
db.session.commit()
```

`db.session.delete(mod_role))` to delete from the DB.

### Query

`Role.query.all()`
`User.query.filter_by(role=user_role).all()`

Inspecting the query `str(User.query.filter_by(role=user_role))`

Query methods:
- `.all()`
- `.first()`
- `.get()`
- `.count()`
- `.paginate()`

Filtering:
- `.filter()`
- `.filter_by()`
- `.limit()`
- `.offset()`
- `.order_by()`
- `.group_by()`

[Querying guide](https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html)




