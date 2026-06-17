#BUSCA BINARIA

Lista = []
encontrado = False


qtd = int(input("Digite a quantidade de itens que a lista tera: "))
print("")
for i in range(qtd):
  num = int(input(f"Digite o {i + 1}º numero da lista: "))
  Lista.append(num)
print(f"\nLista Crua\n{Lista}\n")

Lista.sort()
print(f"\nLista Ordenada\n{Lista}\n")
procura = int(input("Digite um numero para saber se ele esta na lista: "))

inicio = 0
fim = len(Lista) - 1

while inicio <= fim:
  meio = (inicio + fim) // 2
  if Lista[meio] == procura:
    encontrado = True
    break
  elif Lista[meio] < procura:
    inicio = meio + 1
  else:
    fim = meio - 1

if encontrado:
  print(f"\nValor {procura} encontrado pela busca binaria.\nLista: {Lista}")
else:
  print(f"\nValor {procura} nao encontrado pela busca binaria.\nLista: {Lista}")
