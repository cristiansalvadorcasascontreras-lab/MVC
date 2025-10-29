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
class Numero:
    def __init__(self):
        self.dato_numero = 0  # atributo principal

    def get_numero(self):
        return self.dato_numero

    def set_numero(self, nuevo_numero):
        self.dato_numero = nuevo_numero

    def validar_par(self):
        if self.dato_numero % 2 == 0:
            return "El número es par"
        else:
            return "El número es impar"

    def validar_signo(self):
        if self.dato_numero > 0:
            return "El número es positivo"
        elif self.dato_numero < 0:
            return "El número es negativo"
        else:
            return "El número es neutro"

    def validar_numero(self):
        # Combina ambas validaciones
        mensaje_par = self.validar_par()
        mensaje_signo = self.validar_signo()
        return f"{mensaje_par} y {mensaje_signo}"
