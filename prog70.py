class Carros:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = Carros("Toyota", "Corolla")
carro2 = Carros("Renault", "Logan")

print(f"A marca do seu carro é {carro1.marca} e o modelo é {carro1.modelo}")
print(carro2.modelo)