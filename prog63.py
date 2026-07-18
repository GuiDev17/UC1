nomes=["Ana","Marcos","Bruno"] #REMOVE(exclui da lista) , SORT(Coloca em ordem a lista) e LEN(Conta quantos itens tem na lista)
print(f" Listagem de nome {nomes}")

nomes.append("João")

print(f" Listagem de nome atualizada {nomes}")
n=input("Digite o nome a ser excluido: ")
nomes.remove(n)
print(f"Listagem de nome atualizadas {nomes}")
nomes.sort()
print(f"Listagem de nomes ORDENADA {nomes}")
l= len(nomes)
print(f"A lista tem {l} itens")
