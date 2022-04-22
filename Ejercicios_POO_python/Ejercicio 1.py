# Inicializar la clase 
class Persona:
    def __init__(self, name: str) -> None:
        self.nombre = name
    def __str__(self) -> str:
        return "Mi nombre es "+self.nombre

# Instanciar objetos
Persona1 = Persona("Pepe")
Persona2 = Persona("Juan")

# Imprimir objetos
print(Persona1.__str__())
print(Persona2.__str__())