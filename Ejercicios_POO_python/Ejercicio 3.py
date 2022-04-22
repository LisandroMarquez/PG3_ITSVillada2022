# Inicializar la clase
class Triangulo:
    def __init__(self, l1: float, l2: float, l3: float) -> None:
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3
    def ladoMayor(self) -> str:
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return "El lado mayor es "+str(self.lado1)
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            return "El lado mayor es "+str(self.lado2)
        else:
            return "El lado mayor es "+str(self.lado3)
    def equilatero(self) -> str:
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return "El triangulo es equilatero"
        else:
            return "El triangulo no es equilatero"

# Instanciar objetos
triangulo1 = Triangulo(3, 3, 3)
triangulo2 = Triangulo(3, 5, 4)

# Imprimir objetos
print(triangulo1.ladoMayor())
print(triangulo1.equilatero())
print(triangulo2.ladoMayor())
print(triangulo2.equilatero())