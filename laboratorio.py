class Laboratorio():
    def __init__(self, producto):
        self.producto = producto

class Producto():
    def __init__(self, nombre, porcentaje):
        self.nombre = nombre
        self.porcentaje = porcentaje

    def get_nombre(self):
        return self.nombre

    def get_porcentaje(self):
        return self.porcentaje

class Medicamento(Producto):
    def __init__(self, nombre, porcentaje, composicion, precio):
        super().__init__(nombre, porcentaje)
        self.composicion = composicion
        self.precio = precio

    def get_composicion(self):
        return self.composicion

    def get_precio(self):
        return self.precio

prod1 = Medicamento('paracetamol', 0.2, 'analgesico', 10.0)
print(prod1.get_nombre(), prod1.get_precio(), prod1.get_porcentaje(), prod1.get_composicion())
 #Funciona :) yuhuu!
