for i in range(4):
    print(f"Cadastro do {i+1}° aluno")
    nome=input("Digite seu nome: ")
    n1=float(input("Digite a sua primeira nota: "))    
    n2=float(input("Digite a sua segunda nota: "))    
    n3=float(input("Digite a sua terceira nota: "))
    m= (n1+n2+n3)/3
    if m>=7:
        sit= "APROVADO"
    elif m>=5:
        sit= "RECUPERAÇÃO"
    else:
        sit= "REPROVADO"
    print("Nome: ",nome)
    print(f"Suas notas foram:{n1},{n2},{n3}")
    print(f"Sua média final foi {m:.2f}")
    print(f"Sua situação final é {sit}")