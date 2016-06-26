from tornado_jinja2 import Jinja2Loader

import unittest

import jinja2


class LoaderTest(unittest.TestCase):
    templates_path = 'test/templates/'

    def setUp(self):
        self.jinja2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.templates_path))
        self.loader = Jinja2Loader(self.jinja2_env)
        self.template_obj = self.loader.load('page.html')

    def test_load_template(self):
        self.assertIsInstance(self.template_obj, jinja2.Template)

    def test_generete_html(self):
        html_code = self.template_obj.generate(name='hi')
        self.assertIn('hi', html_code)

    def test_get_jinja2_environment(self):
        self.assertIs(self.loader.jinja2_environment, self.loader._jinja2_env)
        self.assertIs(self.loader.jinja2_environment, self.template_obj.environment)

    def test_set_jinja2_environment(self):
        env = jinja2.Environment()
        env.loader = jinja2.FileSystemLoader(self.templates_path)
        self.loader.jinja2_environment = env

        template_obj2 = self.loader.load('page.html')
        self.assertIs(template_obj2.environment, env)

    def test_cached_jinja2_environment(self):
        template_obj2 = self.loader.load('page.html')
        self.assertIs(self.template_obj.environment, template_obj2.environment)

    def test_check_jinja2_environment(self):
        self.loader.jinja2_environment = None
        self.assertRaises(TypeError, self.loader.load, 'page.html')


class LoaderLegacyTest(LoaderTest):
    def setUp(self):
        self.loader = Jinja2Loader(self.templates_path)
        self.template_obj = self.loader.load('page.html')


if __name__ == '__main__':
    unittest.main()
