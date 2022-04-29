# Inicializar la clase 
class Persona:
    def __init__(self, name: str) -> None:
        self.nombre: str = name
    def __str__(self) -> str:
        return f"Mi nombre es {self.nombre}"

# Instanciar objetos
Persona1 = Persona("Pepe")
Persona2 = Persona("Juan")

# Imprimir objetos
print(Persona1)
print(Persona2)