def idade_nasc(ano):
    idade=2026 - ano
    if idade>=65:
        print(f"Sua idade é {idade}, voce é IDOSO")   
    elif idade>=18:
        print(f"Sua idade é {idade}, voce é MAIOR DE IDADE")
    else:
        print(f"Sua idade é {idade}, voce é MENOR DE IDADE")

n1=int(input("Digite seu ano de nascimento: "))
idade_nasc(n1)


