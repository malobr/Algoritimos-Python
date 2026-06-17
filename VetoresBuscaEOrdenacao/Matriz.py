#Vetor de alunos

alunos = []
cores = []
hobbies = []
musicas = []
matriz = []

qtd = int(input("Digite quantos alunos deseja Adicionar a lista: \n"))
print("")

for i in range(qtd):
  linha = []
  aluno = input(f"\nDigite o nome do {i + 1}º Aluno: ")
  alunos.append(aluno)
  linha.append(aluno)
  cor = input(f"Digite a cor favorita do {i + 1}º aluno: ")
  cores.append(cor)
  linha.append(cor)
  hobbie = input(f"Digite o Hobbie do {i + 1}º aluno: ")
  hobbies.append(hobbie)
  linha.append(hobbie)
  musica = input(f"Digite o estilo favorito de musica do {i + 1}º Aluno: ")
  musicas.append(musica)
  linha.append(musica)
  matriz.append(linha)

print("\nA lista de alunos e suas caracteristicas é: \n")
for indice in matriz:
  print(indice)
print(matriz)
print(f"\nLista de nomes: {alunos}")
print(f"Lista de cores: {cores}")
print(f"Lista de Hobbies: {hobbies}")
print(f"Lista de estilos musicais: {musicas}")

