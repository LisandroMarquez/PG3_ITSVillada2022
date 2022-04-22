# Inicializar la clase
class Familia:
    def __init__(self, pa: str, ma: str, hijos: list[str]) -> None:
        self.padre: str = pa
        self.madre: str = ma
        self.hijos: list[str] = hijos
        cont: int = 0
    def imprimir(self) -> None:
        print("Padre de la familia: "+self.padre+"\nMadre de la familia: "+self.madre+"\nHijos de la familia: ")
        for i in range(len(self.hijos)):
            print(f"{i+1}) {self.hijos[i]}")

# Instanciar objetos
familia1 = Familia("Juan", "Maria", ["Pedro", "Juana", "José"])
familia2 = Familia("Gustavo", "Josefina", ["Rodrigo", "Olivia"])

# Imprimir objetos
familia1.imprimir()
familia2.imprimir()