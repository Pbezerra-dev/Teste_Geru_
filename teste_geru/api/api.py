from cornice import Service
from teste_geru.utils.create_sessions import create_id_sessions_api
from pyramid.httpexceptions import HTTPNotFound

sessions_info = Service(name='api1', path="api/v1/sessions")


@sessions_info.get()
def get_info(request):
    """Retorna os ids das sessões do banco de dados"""
    result = create_id_sessions_api(request)
    pks = [pk['browser_session'] for pk in result]
    return {'sessions': pks}


sessions_info_id = Service(name='api_1', path="api/v1/sessions/{pk}")


@sessions_info_id.get()
def get_info_id(request):
    """Retorna apenas os ids da sessão passada em {pk}"""
    pk = request.matchdict['pk'].replace('"', '')

    result = create_id_sessions_api(request)
    pks1 = [ids['browser_session'] for ids in result]
    if pk in pks1:
        pks2 = [value for value in pks1 if value == pk]
        return {'session': pks2}
    else:
        return HTTPNotFound(json={'error': "Not Found"})
