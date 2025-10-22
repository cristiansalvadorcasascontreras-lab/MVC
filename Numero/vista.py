class Vista_formulario:
    def __init__(self):
        self.nombre_modelo = "validar numeros"
        self.texto_pregunta = "digite un numero: "
        self.campo_numero = ""

    def hacer_campo(self):
        print(self.nombre_modelo)
        print(self.texto_pregunta)
        self.campo_numero = int(input())
        return self.campo_numero
    def imprimir_resultado(self, dato_mensaje):
        print(dato_mensaje)
        