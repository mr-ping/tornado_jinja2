# Integrate Jinja2 with Tornado

### How to use:

** Import the jinja2 loader to your project ** 

'''python
from tornado_jinja2 import Jinja2Loader
'''

** Pass the jinja2 loader instance to the "template_loader" parameter of "tornado.web.Application" **

'''python
jinja2loader = Jinja2Loader('templates_path')
settings = dict(template_loader=jinja2loader)
application = tornado.web.Application(**settings)
'''

### Test it

** Execuse the command in the package directory **

    python -m test.test
