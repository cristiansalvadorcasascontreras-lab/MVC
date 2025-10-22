class Controlador:
    def __init__(self, obj_vista , obj_modelo):
        #composicion en el constructor
        self.obj_vista = obj_vista
        self.obj_modelo = obj_modelo


    def hacer_pregunta(self):
        self.obj_formulario.hacer_campo()
        self.obj_numero.validar_par()
        dato_mensaje = self.obj_numero.validar_par()
        
        self.obj_formulario.imprimir_resultado(aux_mensaje)
        