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


class Jinja2Loader(tornado.template.BaseLoader):
    """ inherit form tornado.template.BaseLoader
    Implementing customized Template Loader of for tornado to generate
    Jinja2 template.

    A jinja2.environment.Environment object may be provided using
    `jinja2_environment` argument, it can also be set later using `jinja2_environment`
    property. Additional arguments are passed to tornado.template.BaseLoader.

    A very basic example for a loader that looks up templates on the file
    system could look like this::

        jinja2_environment = jinja2.Environment()
        jinja2_environment.loader = jinja2.FileSystemLoader('/path/to/templates')
        loader = Jinja2Loader(jinja2_environment)
    """

    def __init__(self, *args, **kwargs):
        # Get arguments with backward compatibility
        if args:
            arg = args[0]
            if isinstance(arg, Environment):
                jinja2_environment = arg
                root_directory = None
            else:
                jinja2_environment = None
                root_directory = args
            kwargs.pop('jinja2_environment', None)
            kwargs.pop('root_directory', None)
        else:
            jinja2_environment = kwargs.pop('jinja2_environment', None)
            root_directory = kwargs.pop('root_directory', None)

        if jinja2_environment:  # Env provided
            self._jinja2_env = jinja2_environment
        elif root_directory:  # Backward compatibility
            self._jinja2_env = Environment()
            self._jinja2_env.loader = FileSystemLoader(root_directory)
        else:  # Set env later
            self._jinja2_env = None

        super(Jinja2Loader, self).__init__(**kwargs)

    @property
    def jinja2_environment(self):
        return self._jinja2_env

    @jinja2_environment.setter
    def jinja2_environment(self, env):
        if env is self._jinja2_env:
            return

        # Clear template cache
        with self.lock:
            self._jinja2_env = env
            self.templates = {}

    def resolve_path(self, name, parent_path=None):
        return name  # Template searching should be handled by Jinja2's loader

    def _create_template(self, name):
        if self._jinja2_env is None:
            raise TypeError('no jinja2 environment for this loader specified')
        return self._jinja2_env.get_template(name)
