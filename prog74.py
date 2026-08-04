class Passarinho:
    def __init__(self,raca, cor):
        self.raca = raca
        self.cor = cor

    def canta(self):
        return (f'{self.raca} tem o canto bonito')

passarinho1 = Passarinho("Sabiá", "Marrom")
passarinho2 = Passarinho("Canarinho", "Amarelo")

print(f"{passarinho1.raca} é {passarinho1.cor}")
print(f"{passarinho2.raca} é {passarinho2.cor}")
print(passarinho1.canta())