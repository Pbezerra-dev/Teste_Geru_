from pyramid.view import view_config
from request_api.request import get_quote, get_quotes
from pyramid.httpexceptions import HTTPNotFound

from teste_geru.utils.create_sessions import create_id_session
from random import choice


@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    """Pagina inicial do Projeto"""

    # Salva os dados da sessão no db
    create_id_session(request)
    return {'title': 'Titulo'}


@view_config(route_name='quotes', renderer='templates/quotes.jinja2')
def quotes(request):
    """Retorna todas as citações"""

    # Salva os dados da sessão no db
    create_id_session(request)
    for quotes in get_quotes().values():
        return {'quotes': quotes}


@view_config(route_name='q_num', renderer='templates/q_number.jinja2')
def quote_number(request):
    """Retorna a citação de acordo com o índice passado para o parâmetro {pk}
       Caso não haja o índice informado é retornado um 404 Not Found"""

    try:
        # Captura o id passado na url /{pk}
        pk = request.matchdict['pk']
        # Passa para função get_quotes() o id captuado
        quote = get_quote(pk)

        # Salva os dados da sessão no db
        create_id_session(request)
        return {'quote': quote['quote']}

    except KeyError:
        return HTTPNotFound()


@view_config(route_name='q_random', renderer='templates/q_random.jinja2')
def quote_random(request):
    """Retorna o índice e a citação correspondete de forma pseudo-randômico"""

    # Atribui o indice a citação correspondente
    value = tuple(enumerate(get_quotes()['quotes']))
    # Executa um choice(sorteio) na citação/íncide retornado
    response = choice(value)

    # Salva os dados da sessão no db
    create_id_session(request)
    return {'num': response[0], 'quote': response[1]}
