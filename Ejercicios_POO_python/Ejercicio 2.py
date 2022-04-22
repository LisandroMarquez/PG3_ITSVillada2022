# Inicializar la clase 
class Alumno:
    def __init__(self, nombre: str, nota: int) -> None:
        self.nombre: str = nombre
        self.nota: int = nota
    def __str__(self) -> str:
        return f"Mi nombre es {self.nombre}, mi nota es {str(self.nota)}"
    def Aprobado(self) -> str:
        if self.nota >= 7:
            return "Y estoy aprobado"
        else:
            return "Y estoy desaprobado"

# Instanciar objetos
alumno1 = Alumno("Pepe",4)
alumno2 = Alumno("Lichi", 9)

# Imprimir objetos
print(alumno1.__str__())
print(alumno1.Aprobado())

print(alumno2.__str__())
print(alumno2.Aprobado())