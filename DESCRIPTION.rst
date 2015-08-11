Integrate Jinja2 into Tornado Framework
=======================================

This tool make you have the ability that using jiaja2 Template Engine with Tornado Web Framework.
It will instead of Tornado Templates.

How to use:
-----------

Import the jinja2 loader to your project

.. code-block:: python

    from tornado_jinja2 import Jinja2Loader


Pass the jinja2 loader instance to the "template_loader" parameter which for "tornado.web.Application"

.. code-block:: python

    import tornado.web

    jinja2loader = Jinja2Loader('templates_path')
    settings = dict(template_loader=jinja2loader)

    application = tornado.web.Application(handler=[],
                                        **settings)
