# Import all the models, so that Base has them before being
# imported by Alembic
from app.api.v1.messages.model import Message
from app.api.v1.system_prompts.model import SystemPrompt
from app.db.session import Base, engine


def create_tables() -> None:
    """
    Create database tables.
    """
    Base.metadata.create_all(bind=engine)
