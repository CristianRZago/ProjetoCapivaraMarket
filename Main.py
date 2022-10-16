from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date, Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://root:123456@localhost:3306/ORM"

Base = declarative_base()

class Endereco(Base):
    __tablename__ = "Endereco"
    id_endereco = Column(Integer, primary_key=True)
    rua = Column(String(150), nullable=False)
    n_casa = Column(Integer, nullable=False)
    bairro = Column(String(150), nullable=False)
    cidade = Column(String(150), nullable=False)
    estado = Column(String(150), nullable=False)

    funcionarios = relationship("Funcionario", backref="endereco")


class Funcionario(Base):
    __tablename__ = "Funcionario"
    id_funcionario = Column(Integer, primary_key=True)
    data_Nacimento = Column(Date, nullable=False)
    nome = Column(String(150), nullable=False)

    id_endereco = Column(Integer, ForeignKey("Endereco.id_endereco"))
    dados_contratos = relationship("Dados_Contratuais", backref="funcionario")
    experiencias = relationship("Experiencia", backref="funcionario")
    pontos = relationship("Ponto", backref="funcionario")

class Dados_Contratuais(Base):
    __tablename__ = "Dados_Contratuais"
    id_Dados_Contratuais = Column(Integer, primary_key=True)
    funcao = Column(String(150), nullable=False)
    salario = Column(Integer, nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)

    id_funcionario = Column(Integer, ForeignKey("Funcionario.id_funcionario"))

class Experiencia(Base):
    __tablename__ = "Experiencia"
    id_experiencia = Column(Integer, primary_key=True)
    empresa = Column(String(150), nullable=False)
    funcao = Column(String(150), nullable=False)
    salario = Column(Float, nullable=False)
    data_entrada = Column(Date, nullable=False)
    data_saida = Column(Date, nullable=False)

    id_funcionario = Column(Integer, ForeignKey("Funcionario.id_funcionario"))

class Ponto(Base):
    __tablename__ = "Ponto"
    id_ponto = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    entrada = Column(DateTime, nullable=False)
    saida = Column(DateTime, nullable=False)

    id_funcionario = Column(Integer, ForeignKey("Funcionario.id_funcionario"))


class Login(Base):
    __tablename__ = "Login"
    id_login = Column(Integer, primary_key=True)
    login = Column(String(150), nullable=False)
    senha = Column(String(150), nullable=False)

class Marca(Base):
    __tablename__ = "Marca"
    id_marca = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

class Item(Base):
    __tablename__ = "Item"
    id_item = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    precos = relationship("Preco", backref="item")
    estoques = relationship("Estoque", backref="item")
    armazenamentos = relationship("Armazenamento", backref="item")

class Preco(Base):
    __tablename__ = "Preco"
    id_preco = Column(Integer, primary_key=True)
    preco = Column(Float, nullable=False)
    data_alteracao = Column(DateTime, nullable=False)

    id_item = Column(Integer, ForeignKey("Item.id_item"))

class Estoque(Base):
    __tablename__ = "Estoque"
    id_estoque = Column(Integer, primary_key=True)
    quantidade = Column(Integer, nullable=False)

    id_item = Column(Integer, ForeignKey("Item.id_item"))

class Armazenamento(Base):
    __tablename__ = "Armazenamento"
    id_armazenamento = Column(Integer, primary_key=True)
    local = Column(String(150), nullable=False)
    forma_armazenamento = Column(String(150), nullable=False)

    id_item = Column(Integer, ForeignKey("Item.id_item"))

def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()

