#Pasos paara trabjar en POO

#se organiza en la zona de clases
#1. Identificar las clases
#2. metodos constructor
#3. crear atributos
#4. crear metodos normales --> recibir datos - parametros

#se organiza en la zona principal del codigo
#5. llamar objeto de clase -->enviar datos - (constructor) - argumentos
#6 llamar metodos --> enviar datos -argumentos
#7. retornar en metodos --> Almacenar los datos (variables)

#----------------------------------
#composicion de clases --> llamar objeto en el constructor 
#agregacion clases --> llamar objeto desde el metodo 
#""
class numero:
    def __init__(self):
        self.numero = " "
    def get_numero(self):
        return self.numero
    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero

    def validar_par(self):
        if self.numero % 2 == 0:
            mensaje = "El numero es par"
        else:
            mensaje = "El numero es impar"
        return mensaje