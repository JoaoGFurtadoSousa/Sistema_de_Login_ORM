from models import Users, engine
from sqlmodel import Session, select

usuario = {"nome" : "John",
           "email" :"john@email.com",
           "password" :"teste123"}

usuario= Users(**usuario)

class UsersView:
    @classmethod
    def salvar_no_banco():
        with Session(engine) as session: #session é como se fosse o cursor (bibliotecario)
            session.add(usuario)
            session.commit()

    @classmethod
    def buscar_usuario(cls, id: int):
        with Session(engine) as session:
            usuarios = select(Users).where(Users.id == id)
            usuario_unico = session.exec(usuarios).first()
            print(usuario_unico)

UsersView.buscar_usuario(1)