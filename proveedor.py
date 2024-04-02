from claseBase import *


class Proveedor(ClaseBase):
    def  __init__(self, id, descripcion): 
      super().__init__(id, descripcion)
    
    def get_descripcion(self):
      return super().descripcion
    
    def set_descripcion(self, descripcion):
       super().descripcion = descripcion

    def get_id(self):
      return super().id
    
    def set_id(self, id):
       super().id=id