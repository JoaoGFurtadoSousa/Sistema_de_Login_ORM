from controller import UsuariosController


def exibir_menu():
    escolha_usuario = int(input("Selecione o que quer fazer: \n[1]Cadastro \n[2]Login "))
    match escolha_usuario:
        case 1:
            nome = input("Nome:")
            email = input("Email: ")
            password = input("Password: ")
            usuario = UsuariosController.cadastrar_usuario(nome= nome, email= email, password= password)
            if usuario != True:
                print("Erro ao criar o usuario")
                return False
            print("Usuario criado com sucesso!")
            usuario_login = UsuariosController.login(email= email, password= password)  
            if usuario_login:
                print("Usuario logado com sucesso!")
            else:
                print("Erro ao logar o usuario")
        case 2:
            email = input("Email: ")
            password = input("Password: ")
            usuario = UsuariosController.login(email= email, password= password)
            if usuario:
                return print("Usuario Logado")
            print("Dados invalidos")


exibir_menu()