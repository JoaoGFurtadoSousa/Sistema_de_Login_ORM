from models import Users, engine
from sqlmodel import Session, select
from DAO import UsuariosDAO
import hashlib, re

class UsuariosController:

    @classmethod
    def valida_se_o_email_e_valido(cls, email:str) -> bool:
        validacao_da_string = re.compile('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com')
        validacao_email_valido = re.fullmatch(validacao_da_string, email)
        if validacao_email_valido != None:
            return True
        else:
            print("Insira um email valido.")
            return False

    @classmethod
    def criptografa_password(cls, password: str):
        bytes_password = password.encode("utf-8")
        sha = hashlib.sha256()
        sha.update(bytes_password)
        password_hash = sha.hexdigest()
        return password_hash


    @classmethod
    def cadastrar_usuario(cls, nome: str, email: str, password: str):
        if nome == None or email==None or password==None:
            return False
        email_verificado = cls.valida_se_o_email_e_valido(email= email)
        if email_verificado == True:
            password_criptografada = cls.criptografa_password(password= password)
            UsuariosDAO.salvar_no_banco(Users(nome= nome, email= email, password= password_criptografada))
            return True
        return False

    @classmethod
    def login(cls, email: str, password: str):
        usuario = UsuariosDAO.buscar_usuario(email= email)
        if usuario != False:        
            password_criptografada = cls.criptografa_password(password= password)
            if usuario.password == password_criptografada:
                return True
        return False


