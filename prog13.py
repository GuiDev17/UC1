print("Ola, bem vindo a escola das Laranjeiras!")
nome=input("Qual o seu nome? ")
n1=float(input("Qual foi sua 1º nota? "))
n2=float(input("Qual foi sua 2º nota? "))
n3=float(input("Qual foi sua 3º nota? "))
n4=float(input("Qual foi sua 4º nota? "))
m=(n1+n2+n3+n4)/4
print(f"{nome} sua média final é {m}")
if m>= 6:
    print("APROVADO")
else:
    print("RECUPERAÇÃO")