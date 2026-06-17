numeros = []
lista = []
total = 0

for i in range(5):
  valor = int(input(f"Digite o {i + 1}º numero: "))
  #Adicionando o numero a lista de numeros...
  numeros.append(valor)#adicionando a lista o que o usuario digitou...
#imprimindo a lista de umeros completa
print(numeros)
#imprimindo a lista de nueros, mas um numero por linha..print("\nA lista de numeros é: \n")
for i in range(len(numeros)):
  print(f"{i + 1}º numero: {numeros[i]}")

for e in range(5):
  listaDeNomes = str(input(f"Digite o {e + 1}º Nome: "))
  lista.append(listaDeNomes)
print(lista)
for e in range(len(lista)):
  print(f"{i + 1}º nome: {lista[e]}")

#soma = sum(numeros)
#media = (soma / len(numeros))
#maior = max(numeros)
#menor = min(numeros)

#print(f"\nA soma dos numeros do vetor é: {soma}\nE a media é: {media}\nO maior numero é {maior}\nO menor Numero é: {menor}")
qtd = int(input(f"Digite um numero, para saber a quantidade que ele aparece no vetor: "))
quantidade = numeros.count(qtd)
print(f"\nA quantidade de numeros {qtd} digitadoe é: {quantidade}")

NomeDigitado = str(input(f"Digite um nome, para saber a quantidade vezes que ele aparece no vetor: "))
qtdNome = lista.count(NomeDigitado)
print(f"A quantidade de nomes {NomeDigitado} digitados é: {qtdNome}")
