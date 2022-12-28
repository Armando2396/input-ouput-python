#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
#haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle
class Vehiculo:
    color = ""
    puertas = 0
    Llantas = 0
    Tipo = ""

    def __init__(self, color, puertas, Llantas, Tipo):
        self.color = color
        self.Llantas = Llantas
        self.puertas = puertas
        self.Tipo = Tipo
    
    def getcolor(self):
        return self.color
    
    def getTipo(self):
        return self.Tipo

V1 = Vehiculo("gris", 4, 4, "sedan")
f = open("datos.bin", 'wb')
pickle.dump(V1, f)
f.close()

# ahora leeremos el fichero con el objeto clase

f = open("datos.bin", 'rb')
auto = pickle.load(f)
f.close()

print("Auto \ntipo: ", auto.getTipo(),"\nColor: ", auto.getcolor())
