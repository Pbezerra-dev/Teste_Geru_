import unittest

from pyramid import testing

from sqlalchemy import create_engine
from sqlalchemy.sql import select
from teste_geru.models.model import BrowserSession
from teste_geru.utils.create_sessions import create_id_sessions_api


class ApiSessionsTest(unittest.TestCase):
    """
    Compara se o número de dados da requisição são equivales com DB
    e se os dados dados retornados a requisição são os mesmos do DB
    """

    def setUp(self):
        self.config = testing.setUp()
        self.maxDiff = None

    def test_get_info(self):
        from teste_geru.api.api import get_info

        request = testing.DummyRequest()
        response = get_info(request)
        engine = create_engine('sqlite:///teste_geru.sqlite')
        conn = engine.connect()
        db = select([BrowserSession.browser_session])
        result = conn.execute(db)
        pks1 = [pk['browser_session'] for pk in result]
        pks2 = [pk for pk in response['sessions'] if pk in pks1]
        self.assertEqual(len(pks2), len(pks1))


class ApiSessionIdTest(unittest.TestCase):
    """
    Compara se o número de dados da requisição são equivales com DB
    e se os dados dados retornados a requisição são os mesmos do DB
    filtrando pela a pk passado a url
    """

    def setUp(self):
        self.config = testing.setUp()
        self.maxDiff = None

    def test_get_info_id(self):
        from teste_geru.api.api import get_info_id

        request = testing.DummyRequest(path="api/v1/sessions/{pk}")
        result = create_id_sessions_api(request)
        pks = [pk['browser_session'] for pk in result]
        request.matchdict['pk'] = pks[0]

        response = get_info_id(request)

        pks1 = [pk['browser_session']
                for pk in result if pk in response['session']]
        pks2 = [pk for pk in response['session'] if pk in pks1]
        self.assertEqual(len(pks1), len(pks2))
