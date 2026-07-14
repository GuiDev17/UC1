total=0
valor=1
print("-----COMANDA----- ")
while valor!=0:
    valor=int(input("Digite o valor do produto: "))
    total= total + valor
taxa= total*0.10
vf= taxa + total
print("-----VALOR FINAL-----")
print(f"Valor dos 10%: {taxa}")
print(f"O valor da conta é {vf}R$")
