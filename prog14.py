an=int(input("Qual ano você nasceu? "))
i=2026-an
if i>=65:
    print(f"IDOSO, {i} anos")
elif i>=18:
    print(f"MAIOR DE IDADE, {i} anos")
else:
    print(f"MENOR DE IDADE, {i} anos")