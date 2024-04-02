"""Archvio de script encargado de crear las tablas e ingresar los datos necesarios 
       para poder probar la aplicacion.
       De no tener creada la base de datos se debera ejecutar este script. 
       En caso contrario no es necesario
"""

import sqlite3


def crear_tabla_cheques():
        
        con = sqlite3.connect("cheques.db")
        cursor = con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS cheques
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                fecha_ingreso date NOT NULL,
                id_cliente INTEGER NOT NULL,
                banco varchar(20) NOT NULL,
                id_proveedor INTEGER ,
                numero varchar(20) NOT NULL,
                fecha_pago date NOT NULL,
                id_estado INTEGER NOT NULL,
                importe real NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id),
                FOREIGN KEY (id_proveedor) REFERENCES proveedores(id),
                FOREIGN KEY (id_estado) REFERENCES estados(id)
                )
        """
        cursor.execute(sql)
        con.commit()
        con.close()

    
def crear_tabla_estados():
        con = sqlite3.connect("cheques.db")
        cursor = con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS estados
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 descripcion varchar(20) NOT NULL)
             """
        cursor.execute(sql)
        con.commit()
        con.close()


def crear_tabla_clientes():
        con = sqlite3.connect("cheques.db")
        cursor = con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS clientes
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 descripcion varchar(20) NOT NULL)
             """
        cursor.execute(sql)
        con.commit()
        con.close()


def crear_tabla_proveedores():
        con = sqlite3.connect("cheques.db")
        cursor = con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS proveedores
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 descripcion varchar(20) NOT NULL)
             """
        cursor.execute(sql)
        con.commit()
        con.close()





def datos_tabla_estados(id, descripcion):
        """Funcion que inserta los datos de los estados de los cheques en la base de datos

        Args:
            id (int): id de estado
            descripcion (str): descripcion del estado
        """
        con=sqlite3.connect("cheques.db")
        cursor=con.cursor()
        data=(id, descripcion)
        sql="INSERT INTO estados(id, descripcion) VALUES(?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close()



def datos_tabla_clientes(id, descripcion):
        """Funcion que inserta los datos de los clientes de los cheques en la base de datos

        Args:
            id (int): id de cliente
            descripcion (str): descripcion del cliente
        """
        con=sqlite3.connect("cheques.db")
        cursor=con.cursor()
        data=(id, descripcion)
        sql="INSERT INTO clientes(id, descripcion) VALUES(?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close()


def datos_tabla_proveedores(id, descripcion):
        """Funcion que inserta los datos de los proveedores de los cheques en la base de datos

        Args:
            id (int): id de proveedor
            descripcion (str): descripcion del proveedor
        """
        con=sqlite3.connect("cheques.db")
        cursor=con.cursor()
        data=(id, descripcion)
        sql="INSERT INTO proveedores(id, descripcion) VALUES(?, ?)"
        cursor.execute(sql, data)
        con.commit()
        con.close()


if __name__ == "__main__":
        print("Inicio creacion de tablas y datos") 
        crear_tabla_clientes()
        print("se creo tabla clientes")
        crear_tabla_estados()
        print("se creo tabla estados")
        crear_tabla_proveedores()
        print("se creo tabla proveedores")
        crear_tabla_cheques()
        print("se creo tabla chequqes")
        print("")
        datos_tabla_clientes(1,"cliente 1")
        datos_tabla_clientes(2,"cliente 2")
        print("Datos cargados para clientes")
        datos_tabla_estados(1,"En cartera")
        datos_tabla_estados(2,"Endosado")
        datos_tabla_estados(3,"Depositado")
        print("Datos cargados para estados")        
        datos_tabla_proveedores(1,"proveedor 1")
        datos_tabla_proveedores(2,"proveedor 2")
        print("Datos cargados para proveedores")
        print("Fin")
