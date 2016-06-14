from tornado_jinja2 import Jinja2Loader

import unittest

import jinja2


class LoaderTest(unittest.TestCase):
    def setUp(self):
        templates_path = 'test/templates/'
        self.loader = Jinja2Loader(templates_path, jinja2_env_options={'newline_sequence': '\r\n'})
        self.template_obj = self.loader.load('page.html')

    def test_load_template(self):
        self.assertIsInstance(self.template_obj, jinja2.Template)

    def test_generete_html(self):
        html_code = self.template_obj.generate(name='hi')
        self.assertIn('hi', html_code)

    def test_get_jinja2_environment(self):
        self.assertEqual(self.template_obj.environment, self.loader.get_jinja2_environment())

    def test_cached_jinja2_environment(self):
        template_obj2 = self.loader.load('page.html')
        self.assertEqual(self.template_obj.environment, template_obj2.environment)

    def test_jinja2_env_options(self):
        self.assertEqual(self.loader.get_jinja2_environment().newline_sequence, '\r\n')


if __name__ == '__main__':
    unittest.main()
