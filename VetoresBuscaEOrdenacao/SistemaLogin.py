# sistema de login com as tentativas falhas salvas em uma lista Menu com Cadastro, Login, lista(Somente acessivel logado. Tendo outro MENU onde podemos pesquisar por nome, ou listar todos... se fo admin e remocao no menu da lista), sair
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ESTA INCOMPLETO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#VARIAVEIS DO SITEMA
SenhaCorreta = []
TentativasFalhas = []
nome = []
admin = []
ListAdmin = []
id = []

opc = int

num = 0

UsuarioLogado = None
AdminLogado = False

#FUNCOES DO SISTEMA

def cadastrarUsuario():
  print("--CADASTRO DE USUARIO COMUM--\n")

  n = input("Digite o nome de usuario desejado: ")

  if n in nome:
    print("ERRO!!! Usuario ja existe!!")
    return
  s = int(input("Digite sua senha: "))

  nome.append(n)
  SenhaCorreta.append(s)
  admin.append(False)
  print("Usuario Comum Cadastrado com sucesso!")

def cadastroAdmin():
   print("--CADASTRO DE ADMIN--\n")

   n = input("Digite o nome do Admin desejado: ")

   if n in nome:
    print("ERRO!!! Admin ja existe!!")
    return
   s = int(input("Digite sua senha: "))

   nome.append(n)
   SenhaCorreta.append(s)
   admin.append(True)
   print("Admin Cadastrado com sucesso!")

def loginUsuario():
  global UsuarioLogado, AdminLogado

  if UsuarioLogado is not None:

    sair = input(f"Voce ja esta logado!\nDeseja fazer logout? (s) para sim e (n) para não:\n")

    if sair == "s":
      UsuarioLogado = None
      AdminLogado = False
      print("Logout realizado com sucesso!")
      return

    n = input("\nNome: ")
    s = input("Senha: ")

    if n in nome:
      idx = nome.index(n)
      if SenhaCorreta[idx] == s:
        UsuarioLogado = n
        AdminLogado = AdminLogado[idx]
        print("Login Realizado com Sucesso, Bem vindo(a): {n}")
      else:
        print("Senha incorreta!")
        TentativasFalhas.append(f"Usuario: {n} | Senha errada: {s}")
    else:
      print("Usuario nao encontrado!")
      TentativasFalhas.append(f"Usuario incorreto: {n} | Senha tentada: {s}")


def MenuLista():

  if UsuarioLogado is not None:
    print(f"Erro, Voce precisa estar logado para acerrssar a lista!")
    return

  while True:
    print("\n===SUBMENU: LISTAS E GERENCIAMENTO===")
    print("1 - Pesquisar por nome\n2 - Listar todos os usuarios ")

    if AdminLogado:
      print("3 - Remover um cadastro (Admin)\n4 - Ver tentativas de login falhas (Admin) \n ")
    print("0 - Voltar para o Menu Principal! ")



while True:
  print("\n===SISTEMA=DE=CADASTRO=E=LOGIN===\n")
  print(f"1 - Cadastro\n2 - Login\n3 - Lista\n4 - Sair")

  try:
        opc = int(input("\nDigite a Opção Desejada: \n"))
        print("")
  except ValueError:
        print("Erro: Por favor, digite apenas números!")
        continue

  match opc:
    case 1:

      num = int(input("Escolha que tipo de usuario deseja cadastrar: (Comum | Admin)\n\nPara Admin Digite (1) e para Comum Digite (2)\nOpcao digitada:\n "))

      if num == 1:
        cadastroAdmin()
      elif num == 2:
        cadastrarUsuario()
      else:
        print("\nOpcao invalida!\n")
    case 2:
      loginUsuario()
      print("teste")
    case 3:

      MenuLista()

    case 4:
      print("Saindo...!")
      break
    case _:
      print("\nOpcao invalida!\n")
print("Sistema Encerrado!")



