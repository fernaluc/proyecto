from  baseDatos import *
from cliente import *


class ClienteDB(): 

    def __init__(self): 
        self._bd = BaseDatos()



    def get_all_clientes(self):
        """Funcion que retorna todos los cheques de la base de datos

        Returns:
            [Cliente]: lista de objetos de tipo Cliente
        """
        sql = "SELECT * FROM clientes"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        clientes = []
        for res in resultado:
            cliente = Cliente(res[0],res[1])
            clientes.append(cliente)
        con.close()
        return clientes
    


    def get_cliente_por_id(self, id):
        """Funcion que retona un clinete cuya id sea pasado como parametro

        Args:
            id (int): id del cliente a buscar

        Returns:
            Cliente: objeto de tipo Cliente
        """
        data = (id,)
        sql = "SELECT * FROM clientes where id = ?"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
          
        id_res = resultado[0][0]        
        desc_res = resultado[0][1]
        
        cliente_res = Cliente(id_res,desc_res)
        con.close()
        return cliente_res


    def get_id_cliente(self,descripcion_cliente):
        """Funcion que retonra el id de un cliente cuya descripcion sea la pasada como parametro

        Args:
            descripcion_cliente (str): descripcion del cliente a buscar

        Returns:
            int: id de cliente
        """
        data = (descripcion_cliente,)
        sql = "SELECT id FROM clientes where descripcion = ?"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
        
        id_res = resultado[0][0]        
        con.close()
       
        return id_res



