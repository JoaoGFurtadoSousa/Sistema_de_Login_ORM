from sqlmodel import Field, SQLModel, create_engine
from pydantic import EmailStr


class Users(SQLModel, table= True):
    id: int = Field(primary_key= True)
    nome: str
    email: EmailStr
    password: str


engine = create_engine("sqlite:///usuarios.db", echo= True) #conexão com o bd como se fosse a variavel conexão no sqlite
SQLModel.metadata.create_all(engine)