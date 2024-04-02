from  baseDatos import *
from estado import *


class EstadoDB(): 
    """Clase estado db
    """
    def __init__(self): 
        self._bd = BaseDatos()



    def get_all_estados(self):
        """Funcion que retorna una lista con todos los estados

        Returns:
            [Estado]: lista de objetos de tipo estados
        """
        sql = "SELECT * FROM estados"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        estados = []
        for res in resultado:
            estado = Estado(res[0],res[1])
            estados.append(estado)
        con.close()
        return estados
    


    def get_estado_por_id(self, id):
        """Funcion que retorna un objeto de tipo Estado por un id pasado como parametro

        Args:
            id (int): id del estado a buscar

        Returns:
            Estado: retorna un objeto de tipo Estado
        """
        data = (id,)
        sql = "SELECT * FROM estados where id = ?"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
          
        id_res = resultado[0][0]        
        desc_res = resultado[0][1]
        
        estado_res = Estado(id_res,desc_res)
        con.close()
        return estado_res



    def get_id_estado(self,descripcion_estado):
        """Funcion que retorna un id de un estado cuya descripcion sea la que se pasa como parametro

        Args:
            descripcion_estado (str): descripcion del estado

        Returns:
            int: id del estado
        """
        data = (descripcion_estado,)
        sql = "SELECT id FROM estados where descripcion = ?"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
        
        id_res = resultado[0][0]        
        con.close()
        return id_res




