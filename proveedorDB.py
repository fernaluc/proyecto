from  baseDatos import *
from proveedor import *


class ProveedorDB(): 

    def __init__(self): 
        self._bd = BaseDatos()



    def get_all_proveedores(self):
        """Funcion que retorna una lista con todos los proveedores de la base de datos

        Returns:
            [Proveedor]: lista de objetos de tipo Proveedor
        """
        sql = "SELECT * FROM proveedores"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        proveedores = []
        for res in resultado:
            proveedor = Proveedor(res[0],res[1])
            proveedores.append(proveedor)
        con.close()
        return proveedores
    


    def get_proveedor_por_id(self, id):
        """Funcion que retorna un proveedor cuya id sea el pasado como parametro

        Args:
            id (int): id del proveedor a buscar

        Returns:
            Proveedor: objeto de tipo Proveedor
        """
        data = (id,)
        sql = "SELECT * FROM proveedores where id = ?"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
          
        id_res = resultado[0][0]        
        desc_res = resultado[0][1]
        
        proveedor_res = Proveedor(id_res,desc_res)
        con.close()
        return proveedor_res


#retorna el id de la descripcion del estado pasado como parametro
    def get_id_proveedor(self,descripcion_proveedor):
        """Funcion que retonra un id del proveedor cuya descripcion sea la pasada como parametro

        Args:
            descripcion_proveedor (str): descripcion del proveedor a buscar

        Returns:
            int: id del proveedor
        """
        data = (descripcion_proveedor,)
        sql = "SELECT id FROM proveedores where descripcion = ?"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
        
        id_res = resultado[0][0]        
        con.close()
        
        return id_res



