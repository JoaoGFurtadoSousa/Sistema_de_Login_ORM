from sqlmodel import Field, SQLModel, create_engine
from pydantic import EmailStr


class Users(SQLModel, table= True):
    id: int = Field(primary_key= True)
    nome: str
    email: EmailStr = Field(index= True)
    password: str


engine = create_engine("sqlite:///usuarios.db") #conexão com o bd como se fosse a variavel conexão no sqlite
SQLModel.metadata.create_all(engine)