ListaNum = []

qtd = int(input("Digite a quantidade de idades que a lista tera: "))
for i in range(qtd):
  num = int(input(f"Digite o {i + 1}º numero: "))
  ListaNum.append(num)
print(f"\nIdades na ordem Digitada.\n{ListaNum}")

ListaNum.sort()

print(f"\nIdades por ordem Crescente.\n{ListaNum}")

ListaNum.sort(reverse=True)
print(f"\nIdades em ordem Decrescente.\n{ListaNum}")
