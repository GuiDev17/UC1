carros={}
for i in range(2):
    marca=input("Marca: ")
    carro=input("Modelo: ")
    valor=float(input("Valor: "))
    carros[marca]= {
        "marca": marca,
        "Valor": valor
    }   
    
print(f"Lista de carros: {carros}")