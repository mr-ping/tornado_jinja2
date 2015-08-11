import tornado.template
import jinja2
from jinja2 import Environment, FileSystemLoader


class FixedTemplate(jinja2.Template):
    """ Subclass of jinja2.Template
    Override Template.generate method to adapt render_string method\
            from tornado.RequestHandler
    """
    def generate(self, **kwargs):
        return self.render(**kwargs)

# Change The template class that returned by Environment.get_templte
Environment.template_class = FixedTemplate


class Jinja2Loader(tornado.template.Loader):
    """ inherit form tornado.template.Loader
    Implementing customized Template Loader of for tornado to generate\
            jinja2 template
    """
    def _create_template(self, name):
        env = Environment(loader=FileSystemLoader(self.root))
        return env.get_template(name)

