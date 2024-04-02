import sqlite3




class BaseDatos():
    
    def __init__(self): 
        self._conexion = sqlite3.connect("cheques.db")



   
    @property
    def conexion(self):
        """Funcion que retorna una coneccion a la base de datos

        Returns:
            Connection: coneccion a la base de datos
        """
        self._conexion = sqlite3.connect("cheques.db")
        return self._conexion
       

