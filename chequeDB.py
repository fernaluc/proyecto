from  baseDatos import *
from cheque import *
from proveedor import *
from estado import *
from cliente import *
from clienteDB import *
from estadoDB import *
from proveedorDB import *


class ChequeDB():
    
    def __init__(self): 
        self._bd = BaseDatos()




    def insert_cheque(self,cheque):
        """Funcion que hace un insert en la base de datos del cheque pasado como parametro

        Args:
            cheque (Cheque): objeto de tipo Cheque
        """
        con=self._bd.conexion
        cursor=con.cursor()
        
        proveedor = None
        if (cheque.proveedor is not None ): 
            proveedor = cheque.proveedor.id
        
        data=(cheque.fecha_ingreso, cheque.cliente.id, cheque.banco, proveedor, cheque.nro_cheque, cheque.fecha_pago, cheque.estado.id, cheque.importe)
        sql="INSERT INTO cheques (fecha_ingreso, id_cliente, banco,id_proveedor,numero,fecha_pago,id_estado,importe) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close()



    def delete_cheque_by_id(self, id):
        """Funcion que elimina de la base de datos el cheque con el id pasado como paramtro

        Args:
            id (int): id del cheque a eliminar
        """
        con=self._bd.conexion
        cursor=con.cursor()
        data = (id,)
        sql = "DELETE FROM cheques WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        con.close()


    def update_cheque(self,cheque): 
        """Funcion que hace una actualizacion del los datos del cheque, pasado como parametro, en la base de datos

        Args:
            cheque (Cheque): objeto de tipo Cheque
        """
        con=self._bd.conexion
        cursor=con.cursor() 

        proveedor = None
        if (cheque.proveedor is not None):
            proveedor = cheque.proveedor.id

        data=(cheque.fecha_ingreso, cheque.cliente.id, cheque.banco,proveedor,cheque.nro_cheque,
              cheque.fecha_pago,cheque.estado.id,float(cheque.importe),cheque.id)
        sql="UPDATE cheques set fecha_ingreso = ?, id_cliente = ?, banco = ?, id_proveedor = ?, numero = ?, fecha_pago = ?, id_estado = ?, importe = ? WHERE id =?"
        cursor.execute(sql, data)
        con.commit()
        con.close()



    def get_all_cheques(self):
        """Funcion que retorna una lista con todos los cheques de la base de datos

        Returns:
            [Cheque]: lista de objetos de tipo Cheque
        """
        sql = "SELECT cheques.id, cheques.fecha_ingreso , cheques.id_cliente,\
                cheques.banco, cheques.id_proveedor, cheques.numero,cheques.fecha_pago,\
                cheques.id_estado, cheques.importe,\
                clientes.descripcion, \
                estados.descripcion,\
                proveedores.descripcion\
                FROM cheques \
                INNER JOIN  clientes on cheques.id_cliente = clientes.id \
                INNER JOIN  estados on cheques.id_estado = estados.id \
                LEFT JOIN  proveedores on cheques.id_proveedor = proveedores.id \
                    ORDER BY cheques.fecha_pago DESC"
        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql)

        resultado = datos.fetchall()
        
        
        cheques = []
        for res in resultado:
            id = res[0]
            f_ingreso = res[1]
            id_cliente = res[2]
            banco = res[3]
            id_proveedor = res[4]
            nro = res[5]
            f_pago = res[6]
            id_estado = res[7]
            importe = res[8]
            desc_clietne = res[9]
            desc_estado = res[10]
            desc_proveedor = res[11]

            estado = Estado(id_estado,desc_estado)
            cliente = Cliente(id_cliente,desc_clietne)
                      
            proveedor = None
            if id_proveedor is not None:
                proveedor = Proveedor(id_proveedor,desc_proveedor)
                
            cheque = Cheque(id, f_ingreso, cliente, banco,proveedor,nro,f_pago, estado, importe)
            cheques.append(cheque)
            
        con.close()
        return cheques




    def get_cheque_por_id(self, id):
        """Funcion que retorna un cheque cuyo id sea el pasado como parametro

        Args:
            id (int): id del cheque a buscar
        Returns:
            Cheque: objeto de tipo Cheque
        """
        data = (id,)
        sql = "SELECT cheques.id, cheques.fecha_ingreso , cheques.id_cliente,\
                cheques.banco, cheques.id_proveedor, cheques.numero,cheques.fecha_pago,\
                cheques.id_estado, cheques.importe,\
                clientes.descripcion, \
                estados.descripcion,\
                proveedores.descripcion\
                FROM cheques \
                INNER JOIN  clientes on cheques.id_cliente = clientes.id \
                INNER JOIN  estados on cheques.id_estado = estados.id \
                LEFT JOIN  proveedores on cheques.id_proveedor = proveedores.id \
                    where cheques.id = ?"


        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql, data)
        resultado = datos.fetchall()
        res = resultado[0] #hay un solo resultado
        id = res[0]
        f_ingreso = res[1]
        id_cliente = res[2]
        banco = res[3]
        id_proveedor = res[4]
        nro = res[5]
        f_pago = res[6]
        id_estado = res[7]
        importe = res[8]
        desc_cliente = res[9]
        desc_estado = res[10]
        desc_proveedor = res[11]
            
        
        estado = Estado(id_estado,desc_estado)

        cliente = Cliente(id_cliente,desc_cliente)
        
        proveedor = None
        if id_proveedor is not None:
                proveedor = Proveedor(id_proveedor,desc_proveedor)
                
          
        cheque = Cheque(id, f_ingreso, cliente, banco,proveedor,nro,f_pago, estado, importe)
        con.close()
        return cheque



    def get_cheques_by_filtros(self,id_estado, id_cliente, id_proveedor):
        """Funcion que busca en la base de datos los cheques por estado, cliente y proveedor pasados como paramtros

        Args:
            id_estado (int): id de estado
            id_cliente (int): id de cliente
            id_proveedor (int): id de proveedor

        Returns:
            [Cheque]: lista de objetos de tipo Cheque
        """
        lista_datos = []

        sql = "SELECT cheques.id, cheques.fecha_ingreso , cheques.id_cliente,\
                cheques.banco, cheques.id_proveedor, cheques.numero,cheques.fecha_pago,\
                cheques.id_estado, cheques.importe,\
                clientes.descripcion, \
                estados.descripcion,\
                proveedores.descripcion\
                FROM cheques \
                INNER JOIN  clientes on cheques.id_cliente = clientes.id \
                INNER JOIN  estados on cheques.id_estado = estados.id \
                LEFT JOIN  proveedores on cheques.id_proveedor = proveedores.id \
                    where "

        if (id_estado): 
            sql = sql + " cheques.id_estado = ? "
            lista_datos.append(id_estado)
        if (id_cliente): 
            if len(lista_datos)>0:
                sql = sql + "and cheques.id_cliente = ?"
            else: sql = sql + " cheques.id_cliente = ?"
            lista_datos.append(id_cliente)
        if (id_proveedor):
            if len(lista_datos)>0:
                sql = sql + "and cheques.id_proveedor = ? "
            else: sql = sql + " cheques.id_proveedor = ? "
            lista_datos.append(id_proveedor)
        sql = sql + " ORDER BY cheques.fecha_pago DESC"



        con= self._bd.conexion
        cursor=con.cursor()
        datos=cursor.execute(sql,lista_datos)

        resultado = datos.fetchall()
        
        cheques = []
        for res in resultado:
            id = res[0]
            f_ingreso = res[1]
            id_cliente = res[2]
            banco = res[3]
            id_proveedor = res[4]
            nro = res[5]
            f_pago = res[6]
            id_estado = res[7]
            importe = res[8]
            desc_clietne = res[9]
            desc_estado = res[10]
            desc_proveedor = res[11]

            estado = Estado(id_estado,desc_estado)
            cliente = Cliente(id_cliente,desc_clietne)
                      
            proveedor = None
            if id_proveedor is not None:
                proveedor = Proveedor(id_proveedor,desc_proveedor)
                
            cheque = Cheque(id, f_ingreso, cliente, banco,proveedor,nro,f_pago, estado, importe)
            cheques.append(cheque)
        con.close()
        return cheques


