from sqlalchemy import create_engine
from sqlalchemy.orm import Session as DBsession
from teste_geru.models.model import BrowserSession
from datetime import datetime
import uuid
from sqlalchemy.sql import select


def session_db(request):
    session_request = request.session
    page = request.url

    # Acessa o banco e persiste os dados
    engine = create_engine('sqlite:///teste_geru.sqlite')
    session = DBsession(bind=engine)
    session.add(
        BrowserSession(
            browser_session=str(session_request['id']),
            create_session=datetime.now(),
            page=page,
        )
    )
    session.commit()


def create_id_session(request):
    # Captura os dados necessários
    session_request = request.session

    # Verifica se a sessão ja está com id
    if 'id' in session_request:
        session_db(request)
    else:
        # Cria o Id
        session_request['id'] = uuid.uuid4()
        session_db(request)


def create_id_sessions_api(request):
    # Captura os dados necessários
    session_request = request.session

    # Verifica se a sessão ja está com id
    if 'id' in session_request:
        session_db(request)
    else:
        # Cria o Id
        session_request['id'] = uuid.uuid4()
        session_db(request)

    # Acessa o banco filtrando pela coluna (browser_session)
    engine = create_engine('sqlite:///teste_geru.sqlite')
    conn = engine.connect()
    db = select([BrowserSession.browser_session])
    result = conn.execute(db)
    return result
