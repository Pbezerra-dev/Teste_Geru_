from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

session = SignedCookieSessionFactory(
    'itsaseekreet', httponly=True)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings, session_factory=session) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('cornice')
        config.scan()
    return config.make_wsgi_app()
