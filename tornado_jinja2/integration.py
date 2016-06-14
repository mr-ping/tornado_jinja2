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
    Implementing customized Template Loader of for tornado to generate
    Jinja2 template.

    A dictionary may be passed using `jinja2_env_options` parameter, which
    will be used as keyword arguments to create the Jinja2's Environment object.
    Additional arguments are passed to tornado.template.Loader.
    """

    def __init__(self, root_directory, **kwargs):
        env_options = kwargs.pop('jinja2_env_options') or {}

        super(Jinja2Loader, self).__init__(root_directory, **kwargs)

        env_options['loader'] = FileSystemLoader(self.root)
        self._jinja2_env = Environment(**env_options)

    def get_jinja2_environment(self):
        return self._jinja2_env

    def _create_template(self, name):
        return self._jinja2_env.get_template(name)
