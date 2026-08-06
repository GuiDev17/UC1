print("----ESCOLA PARQUE----")
nome=input("Digite seu nome: ")
n1=float(input("Digite sua 1ª nota: "))
n2=float(input("Digite sua 2ª nota: "))
n3=float(input("Digite sua 3ª nota: "))
n4=float(input("Digite sua 4ª nota: "))
media = (n1+n2+n3+n4)/4
print(f"{nome} sua média final foi {media}")
if media>= 6:
    print("APROVADO!")
else:
    print("REPROVADO!")