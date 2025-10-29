# vista.py
class Vista_formulario:
    def __init__(self):
        self.nombre_modelo = "=== VALIDAR NÚMEROS ==="
        self.texto_pregunta = "Digite un número: "
        self.campo_numero = 0

    def hacer_campo(self):
        print(self.nombre_modelo)
        print(self.texto_pregunta)
        self.campo_numero = int(input())
        return self.campo_numero

    def imprimir_resultado(self, dato_mensaje):
        print("Resultado:", dato_mensaje)
