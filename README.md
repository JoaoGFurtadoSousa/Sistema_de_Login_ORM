Sistema simples de **autenticação de usuários** para cadastro e login via terminal.

### Funcionalidades
- Cadastro de usuários
- Login de usuários
- Validação de e-mail
- Validação de senha (tamanho mínimo)
- Criptografia de senha
- Persistência de dados em banco SQLite

---

## O que é?
Este projeto é uma **aplicação Python executada via terminal**, não é web, desktop com interface gráfica, aplicativo móvel ou biblioteca.

O objetivo do código é **simular um fluxo real de autenticação**, utilizando ORM para manipular dados de usuários em um banco relacional.

---

## Quais tecnologias são usadas?
As principais tecnologias e estruturas utilizadas no projeto são:

- **Python 3.11**
- **SQLModel** (ORM)
- **SQLite** (banco de dados)
- **Arquitetura MVC**
- **DAO (Data Access Object)**
- **hashlib** (criptografia de senha com SHA-256)
- **re (regex)** para validações
- Execução via **terminal**

Essas tecnologias permitem compreender conceitos fundamentais de backend, mesmo sem uso de frameworks web.

---

## Qual é a ambição do projeto?
O projeto tem como objetivo **estudo e aprendizado**, focando em:
- ORM
- organização de código
- separação de responsabilidades
- lógica de autenticação

Não há intenção de lançar este projeto em produção. Ele serve como **base conceitual** para projetos futuros, como APIs com FastAPI ou Django.

---

## Qual é o estágio do projeto?
O projeto está **funcional e concluído para fins educacionais**.

### O que já está feito
- Estrutura MVC definida
- Cadastro e login funcionando
- Validações básicas
- Integração com banco de dados via ORM

### O que poderia ser evoluído
- Melhorar segurança das senhas (salt, bcrypt)
- Criar testes automatizados
- Transformar em API REST
- Remover versionamento do banco SQLite

---

## Existem problemas conhecidos ou limitações?
Sim, algumas limitações são conhecidas e intencionais, por se tratar de um projeto de estudo:

- Uso de **SHA-256 sem salt** (não recomendado para produção)
- Banco SQLite versionado apenas para facilitar testes locais
- Regex de e-mail simplificada
- Ausência de autenticação avançada (JWT, sessões, etc.)

Essas decisões foram tomadas visando **simplicidade e aprendizado**, não uso em produção.

---

## Como executar o projeto

1. Clone o repositório:
  """git clone https://github.com/JoaoGFurtadoSousa/Sistema_de_Login_ORM.git"""

2. Entre na pasta Usuarios:
   cd Sistema_de_Login_ORM\\Usuarios\

3. Execute a aplicação:
   python views.py

   
