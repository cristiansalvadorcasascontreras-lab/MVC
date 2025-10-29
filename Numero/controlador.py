class Controlador:
    def __init__(self, obj_vista, obj_modelo):
        # composición
        self.obj_vista = obj_vista
        self.obj_modelo = obj_modelo

    def ejecutar_programa(self):
        dato_numero = self.obj_vista.hacer_campo()
        self.obj_modelo.set_numero(dato_numero)
        dato_mensaje = self.obj_modelo.validar_numero()
        self.obj_vista.imprimir_resultado(dato_mensaje)
