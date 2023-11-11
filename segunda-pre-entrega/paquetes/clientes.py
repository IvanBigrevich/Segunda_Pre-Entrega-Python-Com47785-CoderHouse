class Cliente:
    def datos(self, nombre, apellido, edad, deudas):
        self.nombre = str(nombre)
        self.apellido = str(apellido)
        self.edad = int(edad)
        self.deudas = str(deudas)

    def bonificacion(datos):
        if self.deudas == "no":
            print("\n\ntiene una bonificacion pendiente para su proxima compra")
        else:
            print("\n\nno tiene una bonificacion pendiente para su proxima compra")