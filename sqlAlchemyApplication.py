from sqlalchemy import Column, JSON, Integer, DECIMAL
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy import select
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()

class Cliente(Base):
    __tablename__ = "data_client"
    
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    cpf = Column(Integer)
    endereco = Column(String(30))
    
    account = relationship(
        "Conta", back_populates="data_client", cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"Client(id={self.id}, name={self.name}, cpf={self.cpf}, endereco={self.endereco})"
    
    
class Conta(Base):
    __tablename__ = "account"
    
    
    id = Column(Integer, primary_key=True)
    tipo = Column(String(30))
    agencia = Column(String(30))
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("data_client.id"))
    
    data_client = relationship("Cliente", back_populates="account")
    
    def __repr__(self) -> str:
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, id_cliente={self.id_cliente}, saldo={self.saldo})"
    
    
print(Cliente.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

with Session(engine) as session:
    Daniel = Cliente(
        name="Daniel Vilela",
        cpf=99999999999,
        endereco="Rua João Perone"
    )
    
session.add_all([Daniel])
session.commit()

stmt = select(Cliente).where(Cliente.name.in_(["Daniel Vilela"]))

for data_client in session.scalars(stmt):
    print(data_client)
    
    
    