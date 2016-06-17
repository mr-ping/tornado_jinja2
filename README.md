# Integrate Jinja2 with Tornado

## Installing:

`pip install tornado-jinja2`

## Using:

Import the jinja2 loader to your project 

```python
from tornado_jinja2 import Jinja2Loader
```

Pass the jinja2 loader instance to the "template_loader" parameter which for "tornado.web.Application"

```python
import tornado.web

jinja2_env = jinja2.Environment()
jinja2_env.loader = jinja2.FileSystemLoader('/path/to/templates')
jinja2_loader = Jinja2Loader(jinja2_env)
settings = dict(template_loader=jinja2_loader)

application = tornado.web.Application(handler=[],
                                      **settings)
```

## Testing

Execuse the command in the package directory

    python -m test.test -v
