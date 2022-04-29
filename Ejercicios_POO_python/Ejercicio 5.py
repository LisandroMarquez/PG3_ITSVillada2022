# Inicializar la clase
class Persona:
    def __init__(self, n: str, e: int) -> None:
        self.nombre: str = n
        self.edad: int = e
    def __str__(self) -> None:
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"

# Instanciar objetos
p1 = Persona("Juan", 36)
p2 = Persona("Pedro", 25)

# Imprimir objetos
print(p1)
print(p2)

# Inicializar la clase
class Empleado(Persona):
    def __init__(self, a: str, b: int) -> None:
        super().__init__(a, b)
        self.sueldo: float = float(input(f"Ingrese el sueldo de {self.nombre}: "))
    def __str__(self) -> None:
        return f"{super().__str__()} \nSueldo: {self.sueldo}\n{self.impuestos()}"
    def impuestos(self) -> None:
        if self.sueldo > 3000:
            return "El empleado debe pagar impuestos"
        else:
            return "El empleado no debe pagar impuestos"

# Instanciar objetos
e1 = Empleado("Lolo", 19)
e2 = Empleado("Mateo", 46)

# Imprimir objetos
print(e1)
print(e2)