class Contador:
    # variable de clase
    contador = 0

    def __init__(self):
        # Incrementa el contador cada vez que se crrea una instancia 
        Contador.contador += 1


# Crear instancias de Contador
c1 = Contador()
c2 = Contador()
c3 = Contador()

print(Contador.contador)


class Coche:
    # Atributo de clase
    cantidad_de_ruedas = 4

    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia

# Crear instancias de Coche
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Focus")

# Acceder al atributo de clase
print(Coche.cantidad_de_ruedas)  # Salida: 4
print(coche1.cantidad_de_ruedas)  # Salida: 4
print(coche2.cantidad_de_ruedas)  # Salida: 4

# Modificar el atributo de clase
Coche.cantidad_de_ruedas = 5

# Verificar el cambio en las instancias
print(Coche.cantidad_de_ruedas)  # Salida: 5
print(coche1.cantidad_de_ruedas)  # Salida: 5
print(coche2.cantidad_de_ruedas)  # Salida: 5