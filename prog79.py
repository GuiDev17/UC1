nascimento=int(input("Digite seu ano de nascmento: "))
idade = 2026 - nascimento
if idade >= 65:
    print(f"Sua idade é {idade}")
    print("PRIORIDADE/SENIOR")
elif idade >= 18:
     print(f"Sua idade é {idade}")
     print("MAIOR DE IDADE")
else:
     print(f"Sua idade é {idade}")
     print("MENOR DE IDADE")