import unittest

from pyramid import testing


class IndexViewTest(unittest.TestCase):
    """Testa se o retorno a requisição é válido"""

    def setUp(self):
        self.config = testing.setUp()

    def test_index(self):
        from teste_geru.views.views import index

        request = testing.DummyRequest()
        response = index(request)
        self.assertEqual(response, {'title': 'Titulo'})


class QuotesViewTest(unittest.TestCase):
    """
    Testa se o retorno a requisição é a lista de citações que é 
    retornada pela api que aplicação consome
    """

    def setUp(self):
        self.config = testing.setUp()
        self.maxDiff = None

    def test_quotes(self):
        from teste_geru.views.views import quotes

        request = testing.DummyRequest()
        response = quotes(request)
        self.assertEqual(response, {'quotes': [
            'Beautiful is better than ugly.',
            'Explicit is better than implicit.',
            'Simple is better than complex.',
            'Complex is better than complicated.',
            'Flat is better than nested.',
            'Sparse is better than dense.',
            'Readability counts.',
            "Special cases aren't special enough to break the rules.",
            'Although practicality beats purity.',
            'Errors should never pass silently.',
            'Unless explicitly silenced.',
            'In the face of ambiguity, refuse the temptation to guess.',
            'There should be one-- and preferably only one --obvious way to do '
            'it.',
            "Although that way may not be obvious at first unless you're "
            'Dutch.',
            'Now is better than never.',
            'Although never is often better than *right* now.',
            "If the implementation is hard to explain, it's a bad idea.",
            'If the implementation is easy to explain, it may be a good idea.',
            "Namespaces are one honking great idea -- let's do more of those!"
        ]})


class QuotsNumberViewsTest(unittest.TestCase):
    """
    Testa se o retorno a requisição é a lista de citações que é 
    retornada pela api que aplicação consome, filtrando pela pk
    passada na url
    """

    def setUp(self):
        self.config = testing.setUp()
        self.maxDiff = None

    def test_quotes_number(self):
        quotes = [
            'Beautiful is better than ugly.',
            'Explicit is better than implicit.',
            'Simple is better than complex.',
            'Complex is better than complicated.',
            'Flat is better than nested.',
            'Sparse is better than dense.',
            'Readability counts.',
            "Special cases aren't special enough to break the rules.",
            'Although practicality beats purity.',
            'Errors should never pass silently.',
            'Unless explicitly silenced.',
            'In the face of ambiguity, refuse the temptation to guess.',
            'There should be one-- and preferably only one --obvious way to do',
            'it.',
            "Although that way may not be obvious at first unless you're",
            'Dutch.',
            'Now is better than never.',
            'Although never is often better than *right* now.',
            "If the implementation is hard to explain, it's a bad idea.",
            'If the implementation is easy to explain, it may be a good idea.',
            "Namespaces are one honking great idea -- let's do more of those!"]

        from teste_geru.views.views import quote_number
        request = testing.DummyRequest(path='/quotes/{pk}')
        request.matchdict['pk'] = 10
        response = quote_number(request)
        self.assertEqual(response, {'quote': quotes[10]})


class QuotesRandomViewsTest(unittest.TestCase):
    """
    Testa se o tipo de dados retornado a requisição são válidos,
    dados válidos = int, str
    """

    def setUp(self):
        self.config = testing.setUp()
        self.maxDiff = None

    def test_quotes_random(self):
        from teste_geru.views.views import quote_random

        request = testing.DummyRequest()
        response = quote_random(request)
        self.assertEqual(type(response['num']) and type(
            response['quote']), type(2) and type('str'))
