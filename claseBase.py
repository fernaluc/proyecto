

#Clase base con id y descripcion como atributos
class ClaseBase:
    
    
    def  __init__(self, id, descripcion): 
      self._id = id
      self._descripcion= descripcion
    
    #getter
    @property
    def id(self): 
         return self._id
       
    #setter 
    @id.setter 
    def id(self, id): 
         self._id = id 

    #getter
    @property
    def descripcion(self): 
         return self._descripcion
       
    #setter 
    @descripcion.setter 
    def descripcion(self, descripcion): 
         self._descripcion = descripcion 