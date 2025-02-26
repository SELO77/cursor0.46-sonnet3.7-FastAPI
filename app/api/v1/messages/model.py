from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.session import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, index=True, nullable=False)
    model = Column(String, nullable=False)
    input_messages = Column(JSON, nullable=False)
    generated_text = Column(Text, nullable=True)
    system_prompt_id = Column(Integer, ForeignKey("system_prompts.id"), nullable=True)
    message_metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    system_prompt = relationship("SystemPrompt")
