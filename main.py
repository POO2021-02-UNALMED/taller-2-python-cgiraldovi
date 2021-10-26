class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(cls, color):
        if(color == "rojo"):
            cls.color = color
        elif(color == "verde"):
            cls.color = color;
        elif(color == "amarillo"):
            cls.color = color
        elif(color == "negro"):
            cls.color = color
        elif(color == "blanco"):
            cls.color = "blanco"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(cls, registro):
        cls.registro = registro


    def asignarTipo(cls,tipo):

        if(tipo == "gasolina"):
            cls.tipo = "gasolina"
        elif(tipo == "electrico"):
            cls.tipo = "electrico";



class Auto:

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = len(asientos)


    def cantidadAsientos(self):
        cont = 0
        for asiento in self.asientos:
            if(asiento is None):
                cont = cont + 0
            else:
                cont = cont + 1
        return cont

    def verificarIntegridad(self):
        cont = 0
        contAsientos = 0;
        for asiento in self.asientos:
            if(asiento is None):
                contAsientos = contAsientos + 0
            else :
                contAsientos = contAsientos + 1
                if(asiento.registro == self.registro):
                    if(self.registro == self.motor.registro):
                        cont = cont + 1


        if(cont == contAsientos):
            return "Auto original"
        else:
            return "Las piezas no son originales"
