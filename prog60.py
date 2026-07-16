def ng(n1,n2,n3,n4):
    media=(n1+n2+n3+n4)/4
    if media>=7:
        print(f"APROVADO,sua media foi {media}")
    elif media>=5:
        print(f"RECUPERAÇÂO, sua media foi {media}")
    else:
        print(f"REPROVADO, sua media foi {media}")

n1=float(input("Digite a 1° nota: "))
n2=float(input("Digite a 2° nota: "))
n3=float(input("Digite a 3° nota: "))
n4=float(input("Digite a 4° nota: "))
ng(n1,n2,n3,n4)

