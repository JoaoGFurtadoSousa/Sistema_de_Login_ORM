from controller import UsuariosController


def exibir_menu():
    escolha_usuario = int(input("Selecione o que quer fazer: \n[1]Cadastro \n[2]Login "))
    match escolha_usuario:
        case 1:
            nome = input("Nome:")
            email = input("Email: ")
            password = input("Password: ")
            usuario = UsuariosController.salvar_usuario(nome= nome, email= email, password= password)
            if usuario != True:
                print("Erro ao criar o usuario")
                return False
            print("Usuario criado com sucesso!")


exibir_menu()