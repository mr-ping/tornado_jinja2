from res.integration import Jinja2Loader

import unittest

import jinja2


class LoaderTest(unittest.TestCase):
    def setUp(self):
        templates_path = 'test/templates/'
        self.template_obj = Jinja2Loader(templates_path).load('page.html')

    def test_load_template(self):
        self.assertIsInstance(self.template_obj, jinja2.Template)

    def test_generete_html(self):
        html_code = self.template_obj.generate(name='hi')
        self.assertIn('hi', html_code)


if __name__ == '__main__':
    unittest.main()
