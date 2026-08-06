total=0
valor=1
while valor != 0:
    valor=int(input("Digite um valor: "))
    total= valor + total
taxa= total * 0.10
vf= taxa + total
print(f"O valor da taxa é {taxa}")
print(f"O total foi {total}")
print(f"o valor final foi de {vf}") 