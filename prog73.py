class Biscoito:
    def __init__ (self, sabor, gosto):
      self.sabor = sabor
      self.gosto = gosto

    def  croc(self):
        return f'{self.sabor} faz croc croc'

biscoito1 = Biscoito("Chocolate", "Morango")
biscoito2 = Biscoito("Pistache", "Limão")

print(f"O biscoito de sabor {biscoito1.sabor} e gosto de {biscoito1.gosto}")
print(f"O biscoito de sabor {biscoito2.sabor} e gosto de {biscoito2.gosto}")
print(biscoito1.croc())