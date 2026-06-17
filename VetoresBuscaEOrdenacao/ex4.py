#Verificando se algo esta ou nao na lista.

ListaIdades = []
encontrado = False

qtd = int(input("Digite a quantidade de idades dejesa adicionar a lista: "))

for i in range(qtd):
  idade = int(input(f"Digite a {i + 1}ª idade: "))
  ListaIdades.append(idade)
print(f"\n",ListaIdades, "\n")

procura = int(input("Digite uma idade para saber se ela esta na lista: "))

for i in ListaIdades:
  if i == procura:
    encontrado = True
    break
if encontrado:
  print(f"\nIdade {procura} encontrada na lista: {ListaIdades}")
else:
  print(f"\nA idade digitada {procura} nao estava na lista..{ListaIdades}")




