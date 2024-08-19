#crear una clase fabrica que tenga los atributos llantas, color y precio; luego crear dos clases mas que hereden, las cuales son moto y carro, crear metodos que muestren la cantidad de llantas color y precio

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_llantas(self):
        return f"Cantidad de llantas: {self.llantas}"

    def mostrar_precio(self):
        return f"Precio: ${self.precio}"

    def mostrar_color(self):
        return f"Color: {self.color}"


class Moto(Fabrica):
    def __init__(self, llantas, color, precio, tipo_moto):
        super().__init__(llantas, color, precio)
        self.tipo_moto = tipo_moto

    def mostrar_tipo_moto(self):
        return f"Tipo de moto: {self.tipo_moto}"


class Auto(Fabrica):
    def __init__(self, llantas, color, precio, marca):
        super().__init__(llantas, color, precio)
        self.marca = marca

    def mostrar_marca(self):
        return f"Marca: {self.marca}"
    
moto1 = Moto(2, "Rojo", 1500, "Deportiva")
auto1 = Auto(4, "Azul", 20000, "Toyota")

print(moto1.mostrar_llantas())
print(moto1.mostrar_precio())
print(moto1.mostrar_color())
print(moto1.mostrar_tipo_moto())

print(auto1.mostrar_llantas())
print(auto1.mostrar_precio())
print(auto1.mostrar_color())
print(auto1.mostrar_marca())