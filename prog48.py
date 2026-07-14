total= 0
codigo=""
print("TABELA DE PREÇOS")
print("001 -> Arroz(R$ 4.00)")
print("002 -> Feijão(R$ 7.00)")
print("003 -> Macarrão(R$ 5.00)")
while codigo !="0":
    codigo=input("Digite o codigo do produto: ")
    if codigo=="001":
        total+=4
        print("001 -> Arroz(R$ 4.00)")
    elif codigo=="002":
        total+=7
        print("002 -> Feijão(R$ 7.00)")
    elif codigo=="003":
        total+=5
        print("003 -> Macarrão(R$ 5.00)")
    else:
        total+=0
        print("Código Inválido")
    
print("Compra finalizada.")    
print(f"O total da compra é de {total}R$")
      
