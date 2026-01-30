from models import Users, engine
from sqlmodel import Session, select

class UsuariosDAO:
    @classmethod
    def salvar_no_banco(cls, usuario: Users):
        with Session(engine) as session: #session é como se fosse o cursor (bibliotecario)
            session.add(usuario)
            session.commit()


    @classmethod
    def buscar_usuario(cls, email: str):
        with Session(engine) as session:
            usuarios = select(Users).where(Users.email == email)
            usuario_unico = session.exec(usuarios).first()
            print(usuario_unico)
            if usuario_unico:
                return usuario_unico
            return False