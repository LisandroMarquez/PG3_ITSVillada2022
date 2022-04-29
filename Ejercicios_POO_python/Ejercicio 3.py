# Inicializar la clase
class Triangulo:
    def __init__(self, l1: float, l2: float, l3: float) -> None:
        self.lado1: float = l1
        self.lado2: float = l2
        self.lado3: float = l3
    def ladoMayor(self) -> str:
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return f"El lado mayor es {self.lado1}"
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            return f"El lado mayor es {self.lado2}"
        else:
            return f"El lado mayor es {self.lado3}"
    def equilatero(self) -> str:
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return "El triangulo es equilatero"
        else:
            return "El triangulo no es equilatero"
    def __str__(self) -> str:
        return f"{self.ladoMayor()}\n{self.equilatero()}"

# Instanciar objetos
triangulo1 = Triangulo(3, 3, 3)
triangulo2 = Triangulo(3, 5, 4)

# Imprimir objetos
print(triangulo1)
print(triangulo2)