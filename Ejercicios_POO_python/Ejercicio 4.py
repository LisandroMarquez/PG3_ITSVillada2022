# Inicializar la clase
class Operaciones:
    def __init__(self, n1: int, n2: int) -> None:
        self.num1: int = n1
        self.num2: int = n2
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    def suma(self) -> None:
        print(f"La suma entre {str(self.num1)} y {str(self.num2)} da: {str(self.num1 + self.num2)}")
    def resta(self) -> None:
        print(f"La resta entre {str(self.num1)} y {str(self.num2)} da: {str(self.num1 - self.num2)}")
    def multiplicacion(self) -> None:
        print(f"La multiplicación entre {str(self.num1)} y {str(self.num2)} da: {str(self.num1 * self.num2)}")
    def division(self) -> None:
        print(f"La división entre {str(self.num1)} y {str(self.num2)} da: {str(self.num1 / self.num2)}")

# Instanciar e imprimir objetos
op1 = Operaciones(8, 2)
op2 = Operaciones(10, 5)