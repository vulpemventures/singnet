from sqlalchemy import Column, DateTime, Integer, Sequence, String, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Agent(Base):
    __tablename__ = 'agents'
    id = Column(Integer, Sequence('agent_id_seq'), primary_key=True, nullable=False)
    agent_id = Column(String(40), nullable=False)
    timestamp = Column(DateTime(), server_default=func.now(), nullable=False)


class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, Sequence('service_id_seq'), primary_key=True, nullable=False)
    agent_id = Column(Integer, ForeignKey('agents.id'))
    ontology_node_id = Column(String(40), nullable=False)
    timestamp = Column(DateTime(), server_default=func.now(), nullable=False)
