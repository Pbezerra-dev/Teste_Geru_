from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class BrowserSession(Base):
    __tablename__ = 'browsersession'
    id = Column(Integer, primary_key=True, )
    browser_session = Column(Text)
    create_session = Column(Text)
    page = Column(Text)
