from tkinter import Entry, Frame, StringVar, DoubleVar, IntVar, Label,Button,ttk
import tkinter as tk
from estadoDB import *
from chequeDB import *
from clienteDB import *
from proveedorDB import *
from baseDatos import *
from validacion_campos import *



class Vista3():
    

    def __init__(self,root):
        self.root = root
        self.root.title("Administrador de cheques")


        ######################### DEFINICION DE FRAMES PRINCIPALES
        #frame de filtros
        self.frame1 = Frame(self.root)

        #frame de lista
        self.frame2 = Frame(self.root, background="green")


        # Ubicar los frames en la ventana usando grid
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=1, column=0, sticky="nsew")

        # Configurar el sistema de grid para que los frames se redimensionen con la ventana
        self.root.grid_columnconfigure(0, weight=1)

        # Configurar el comportamiento de las filas
        self.root.grid_rowconfigure(0, weight=0)  # Fila 0
        self.root.grid_rowconfigure(1, weight=1)  # Fila 1

        #Definicion de varilables
        self.e_fecha_ingreso  = StringVar()
        self.e_banco   = StringVar()
        self.e_nro_orden = IntVar()
        self.e_nro_cheque    = StringVar()
        self.e_importe   = DoubleVar()
        self.e_fecha_pago   = StringVar()


        #combo estado para alta y modificacion
        self.seleccion_estado = StringVar() 
        self.estadoDB = EstadoDB()
        self.estados = self.estadoDB.get_all_estados()
        self.desc_estados = []
        for estado in self.estados:
            self.desc_estados.append(estado.descripcion)
        self.seleccion_estado.set(self.desc_estados[0])

        #combo cliente para alta y modificacion
        self.seleccion_cliente = StringVar() 
        self.clienteDB = ClienteDB()
        self.clientes = self.clienteDB.get_all_clientes()
        self.desc_clientes = []
        for cliente in self.clientes:
            self.desc_clientes.append(cliente.descripcion)
        self.seleccion_cliente.set(self.desc_clientes[0])

        #combo proveedor para alta y modificacion
        self.seleccion_proveedor = StringVar() 
        self.proveedorDB = ProveedorDB()
        self.proveedores = self.proveedorDB.get_all_proveedores()
        self.desc_proveedores = []
        for proveedor in self.proveedores:
            self.desc_proveedores.append(proveedor.descripcion)


        #combos de busquedas
        self.seleccion_estado_busqueda = StringVar() 
        self.seleccion_cliente_busqueda = StringVar()
        self.seleccion_proveedor_busqueda = StringVar()


        ############################################################### FRAME FILTROS
        self.label_fecha_ingreso = Label(self.frame1, text="Fecha de ingreso")
        self.label_fecha_ingreso.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
        self.entry_fecha_ingreso = Entry(self.frame1,textvariable =self.e_fecha_ingreso)
        self.entry_fecha_ingreso.insert(0, "dd-mm-aaaa")
        self.entry_fecha_ingreso.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.label_cliente = Label(self.frame1, text="Cliente")
        self.label_cliente.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)
        self.combo_cliente = ttk.Combobox(self.frame1, values=self.desc_clientes,width=7,textvariable=self.seleccion_cliente,state="readonly")
        self.combo_cliente.grid(row=0, column=4, sticky="nsew", padx=10, pady=10)

        self.label_banco = Label(self.frame1, text="Banco")
        self.label_banco.grid(row=0, column=5, sticky="nsew", padx=10, pady=10)
        self.entry_banco = Entry(self.frame1,textvariable =self.e_banco)
        self.entry_banco.grid(row=0, column=6, sticky="nsew", padx=10, pady=10)

        self.label_proveedor = Label(self.frame1, text="Proveedor")
        self.label_proveedor.grid(row=0, column=7, sticky="nsew", padx=10, pady=10)
        self.combo_proveedor = ttk.Combobox(self.frame1, values=self.desc_proveedores,width=7,textvariable=self.seleccion_proveedor)
        self.combo_proveedor.grid(row=0, column=8, sticky="nsew", padx=10, pady=10)

        self.label_nro_orden = Label(self.frame1, text="Nro Orden")
        self.label_nro_orden.grid(row=0, column=9, sticky="nsew", padx=10, pady=10)
        self.entry_nro_orden = Entry(self.frame1,textvariable =self.e_nro_orden,state="readonly")
        self.entry_nro_orden.grid(row=0, column=10, sticky="nsew", padx=10, pady=10)

        self.label_nro_cheque = Label(self.frame1, text="Nro Cheque")
        self.label_nro_cheque.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.entry_nro_cheque = Entry(self.frame1,textvariable =self.e_nro_cheque)
        self.entry_nro_cheque.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        self.label_importe = Label(self.frame1, text="Importe")
        self.label_importe.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)
        self.entry_importe = Entry(self.frame1,textvariable =self.e_importe)
        self.entry_importe.grid(row=1, column=4, sticky="nsew", padx=10, pady=10)

        self.label_fecha_pago = Label(self.frame1, text="Fecha pago")
        self.label_fecha_pago.grid(row=1, column=5, sticky="nsew", padx=10, pady=10)
        self.entry_fecha_pago = Entry(self.frame1,textvariable =self.e_fecha_pago)
        self.entry_fecha_pago.insert(0, "dd-mm-aaaa")
        self.entry_fecha_pago.grid(row=1, column=6, sticky="nsew", padx=10, pady=10)

        self.label_estado = Label(self.frame1, text="Estado")
        self.label_estado.grid(row=1, column=7, sticky="nsew", padx=10, pady=10)
        self.combo_estado = ttk.Combobox(self.frame1, values=self.desc_estados,width=7,textvariable=self.seleccion_estado,state="readonly")
        self.combo_estado.grid(row=1, column=8, sticky="nsew", padx=10, pady=10)

        self.b_alta = Button(self.frame1, text="Alta", command=lambda:self.alta_cheque(self.e_fecha_ingreso.get(), self.seleccion_cliente.get(), self.e_banco.get(),self.seleccion_proveedor.get(),self.e_nro_cheque.get(),self.e_importe.get(),self.e_fecha_pago.get(),self.seleccion_estado.get(),self.tree))
        self.b_alta.grid(row=1, column=9)                                                

        self.b_modificar= Button(self.frame1, text="Modoficacion", command=lambda:self.modificar(self.e_fecha_ingreso.get(), self.seleccion_cliente.get(), self.e_banco.get(),self.seleccion_proveedor.get(),self.e_nro_cheque.get(),self.e_importe.get(),self.e_fecha_pago.get(),self.seleccion_estado.get(),self.e_nro_orden.get(),self.tree))
        self.b_modificar.grid(row=1, column=10) 

        self.b_limpiar = Button(self.frame1, text="Limpiar", command=lambda:self.limpiar())
        self.b_limpiar.grid(row=1, column=12, padx=5, pady=0) 

        self.label_error = Label(self.frame1, text="Error en el ingreso de datos")
        self.label_error.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.label_error.grid_remove()
        ################################################################# FRAME LISTA

        self.tree = ttk.Treeview(self.frame2)

        self.b_label_estado = Label(self.frame2, text="Estado")
        self.b_label_estado.grid(row=0, column=0, sticky="nsew", padx=5, pady=(30,5))
        self.combo_estado_busqueda = ttk.Combobox(self.frame2, values=self.desc_estados,textvariable=self.seleccion_estado_busqueda)
        self.combo_estado_busqueda.grid(row=0, column=1, sticky="nsew", padx=5, pady=(30,5))

        self.b_label_cliente = Label(self.frame2, text="Cliente")
        self.b_label_cliente.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.combo_cliente_busqueda = ttk.Combobox(self.frame2, values=self.desc_clientes,textvariable=self.seleccion_cliente_busqueda)
        self.combo_cliente_busqueda.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.b_label_proveedor = Label(self.frame2, text="Proveedor")
        self.b_label_proveedor.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.combo_proveedor_busqueda = ttk.Combobox(self.frame2, values=self.desc_proveedores,textvariable=self.seleccion_proveedor_busqueda)
        self.combo_proveedor_busqueda.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        self.b_buscar = Button(self.frame2, text="Buscar", command=lambda:self.buscar(self.seleccion_estado_busqueda.get(),self.seleccion_cliente_busqueda.get(),self.seleccion_proveedor_busqueda.get(),self.tree))
        self.b_buscar.grid(row=2, column=2, padx=5, pady=0) 

        self.b_restaurar_busqueda= Button(self.frame2, text="Restaurar busqueda", command=lambda:self.actualizar_tree(self.tree))
        self.b_restaurar_busqueda.grid(row=2, column=3) 


        # defino columnas
        self.columns = ('fecha_ingreso', 'cliente', 'banco','proveedor','nro_cheque','fecha_pago', 'estado', 'importe')

        self.tree = ttk.Treeview(self.frame2,selectmode="browse") #browse es seleccion simple
        self.tree["columns"] = self.columns
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("fecha_ingreso", width=100, minwidth=100)
        self.tree.column("cliente", width=100, minwidth=100)
        self.tree.column("banco", width=100, minwidth=100)
        self.tree.column("proveedor", width=100, minwidth=100)
        self.tree.column("nro_cheque", width=100, minwidth=100)
        self.tree.column("importe", width=100, minwidth=100)
        self.tree.column("fecha_pago", width=100, minwidth=100)
        self.tree.column("estado", width=100, minwidth=100)

        # defino headings
        self.tree.heading("#0", text="ID")
        self.tree.heading('fecha_ingreso', text='Fecha ingreso')
        self.tree.heading('cliente', text='Cliente')
        self.tree.heading('banco', text='Banco')
        self.tree.heading('proveedor', text='Proveedor')
        self.tree.heading('nro_cheque', text='Nro Cheque')
        self.tree.heading('importe', text='Importe')
        self.tree.heading('fecha_pago', text='Fecha Pago')
        self.tree.heading('estado', text='Estado')
        self.tree.grid(row=10, column=0, columnspan=4, pady=50, padx=50)

        self.b_obtener_datos = Button(self.frame2, text="Obtener Datos", command=lambda:self.obterner_datos(self.tree))
        self.b_obtener_datos.grid(row=11, column=0, padx=5, pady=0) 

        self.b_baja= Button(self.frame2, text="Baja", command=lambda:self.baja_cheque(self.tree))
        self.b_baja.grid(row=11, column=1) 

       
        self.actualizar_tree(self.tree)

    

    
    def ocultar_error(self): 
        """Ocualta el label de error 
        """
        self.label_error.grid_remove()
    def mostrar_error(self): 
        """Funcion que hacer visible el label del error 
        """
        self.label_error.grid()



    def actualizar_tree(self,tv):
        """Funcion que actualiza los valores del treeview con los datos de todos los cheques de la base

        Args:
            tv (Treeview): treeview a actualizar
        """
        records = tv.get_children()
        for element in records:
            tv.delete(element)

        chequeDB = ChequeDB()
        cheques = chequeDB.get_all_cheques()

        for cheque in cheques:
            proveedor = ""
            if cheque.proveedor is not None : 
                proveedor = cheque.proveedor.descripcion
            
            tv.insert("", "end", text=cheque.id, values=(cheque.fecha_ingreso, cheque.cliente.descripcion, cheque.banco,proveedor, cheque.nro_cheque, cheque.fecha_pago, cheque.estado.descripcion, cheque.importe)) 
            #columns = ('fecha_ingreso', 'cliente',                 'banco','proveedor','nro_cheque','fecha_pago', 'estado', 'importe')



    def actualizar_tree_busqueda(self,cheques, tv): 
        """Fucion que Actualiza el treeview con los cheques pasados como parametro

        Args:
            cheques ([Cheque]): lista de objetos de tipo Cheque
            tv (Treeview): treeview a actualizar
        """
        records = tv.get_children()
        for element in records: 
            tv.delete(element)
        
        for cheque in cheques:
            proveedor = ""
            if cheque.proveedor is not None : 
                proveedor = cheque.proveedor.descripcion
            
            tv.insert("", "end", text=cheque.id, values=(cheque.fecha_ingreso, cheque.cliente.descripcion, cheque.banco,proveedor, cheque.nro_cheque, cheque.fecha_pago, cheque.estado.descripcion, cheque.importe)) 
            #columns = ('fecha_ingreso', 'cliente',                 'banco','proveedor','nro_cheque','fecha_pago', 'estado', 'importe')


 
    def get_id_estado(self,descripcion_estado):
        """Funcion que retorna el id del estadado segun la descripcion pasada como parametro

        Args:
            descripcion_estado (str): descripcion del estado

        Returns:
            int: id del estado segun la descripcion
        """
        estadoDB = EstadoDB()
        return estadoDB.get_id_estado(descripcion_estado)


    def get_id_cliente(self,descripcion_cliente):
        """Funcion que retorna el id del cliente segun la descripcion pasada como parametro

        Args:
            descripcion_cliente (str): descripcion del cliente a buscar

        Returns:
            int: id del cliente segun su descripcion
        """
        clienteDB = ClienteDB()
        return clienteDB.get_id_cliente(descripcion_cliente)


    def get_id_proveedor(self,descripcion_proveedor):
        """Funcion que retorna el id del proveedor segun la descripcion pasada como parametro

        Args:
            descripcion_proveedor (str): descripcion del proveedor a buscar

        Returns:
            int: id del proveedor segun su descripcion. Retorna None si no encuentra proveedor
        """
        proveedorDB = ProveedorDB()
        
        if len(descripcion_proveedor)>0: 
            return (proveedorDB.get_id_proveedor(descripcion_proveedor))
        else:  
            return None 
            

    


    def alta_cheque(self,fecha_ingreso, cliente_desc, banco,proveedor_desc,nro_cheque,importe,fecha_pago,estado_desc,tv): 
        """Funcion que hace el alta del cheque en el sistema y actualiza el treeview

        Args:
            fecha_ingreso (str): fecha de ingreso
            cliente_desc (str): descripcion del cliente
            banco (str): nombre del banco
            proveedor_desc (str): descripcion del proveedor
            nro_cheque (str): numero de cheque
            importe (float): importe del cheque
            fecha_pago (str): fecha de pago 
            estado_desc (str): descripcion del estado del cheque
            tv (Treeview): treeview a modificar
        """
        try:
            if Validacion_campos.es_error_fecha(fecha_ingreso) or Validacion_campos.es_error_fecha(fecha_pago):    
                self.mostrar_error() 
            else:
                estado = Estado(self.get_id_estado(estado_desc),estado_desc)
                cliente = Cliente(self.get_id_cliente(cliente_desc),cliente_desc)
                
                proveedor = None
                if proveedor_desc is not None:  
                    proveedor = Proveedor(self.get_id_proveedor(proveedor_desc) ,proveedor_desc)
                
                cheque = Cheque(None,fecha_ingreso,cliente,banco,proveedor,nro_cheque,fecha_pago,estado,importe )
                
                chequeDB = ChequeDB()
                chequeDB.insert_cheque(cheque)
                
                self.actualizar_tree(tv)
                self.limpiar()
        except Exception as e: 
            self.mostrar_error()    
            print("Error en alta de cheque ",type(e)) 




    def baja_cheque(self,tv): 
        """Funcion que toma el valor de la seleccion del treeview y lo elimina del sistema y del treeview 

        Args:
            tv (Treeview): treeview a modificar
        """
        try:
            valor = tv.selection()
            item = tv.item(valor)
            mi_id = item['text']
            chequeDB = ChequeDB()
            chequeDB.delete_cheque_by_id(int(mi_id))
            tv.delete(valor)
        except Exception as e: print("Error en baja de cheque ",type(e)) 





    def modificar(self,fecha_ingreso, cliente_desc, banco,proveedor_desc,nro_cheque,importe,fecha_pago,estado_desc,nro_orden,tv): 
        """Funcnion que modifica los datos del cheque seleccionado actualizando el treeview con los mismos

        Args:
            fecha_ingreso (str): fecha de ingreso
            cliente_desc (str): descripcion del cliente
            banco (str): nombre del banco
            proveedor_desc (str): descripcion del proveedor
            nro_cheque (str): numero de cheque
            importe (float): importe del cheque
            fecha_pago (str): fecha de pago del cheque
            estado_desc (str): descripcion del estado del cheque
            nro_orden (str): nro de orden del cheque (id)
            tv (Treeview): treeview a modificar
        """
        try:
            if Validacion_campos.es_error_fecha(fecha_ingreso) or Validacion_campos.es_error_fecha(fecha_pago):    
                self.mostrar_error() 
            else:
                estado = Estado(self.get_id_estado(estado_desc),estado_desc)
                cliente = Cliente(self.get_id_cliente(cliente_desc),cliente_desc)

                proveedor = None
                if proveedor_desc is not None or len(proveedor_desc>0): 
                    proveedor = Proveedor(self.get_id_proveedor(proveedor_desc) ,proveedor_desc)
                                
                cheque = Cheque(nro_orden,fecha_ingreso,cliente,banco,proveedor,nro_cheque,fecha_pago,estado,importe )
                
                chequeDB = ChequeDB()
                chequeDB.update_cheque(cheque)
                
                self.actualizar_tree(tv)
                self.limpiar()
        except Exception as e: 
            self.mostrar_error()
            print("Error en modifcar cheque ",type(e)) 





    def buscar(self,estado_desc, cliente_desc, proveedor_desc,tv): 
        """Funcion que busca los cheques segun el estado, descripcion y/o proveedor. Si no encuentra criterios de busqueda muestra todos los cheques

        Args:
            estado_desc (str): descripcion del estado
            cliente_desc (str): descripcion del cliente
            proveedor_desc (str): descripcion del proveedor
            tv (Treeview): treeview a modificar
        """
        try:
            if (not estado_desc and not proveedor_desc and not cliente_desc):
                #mostrar todos los datos de la tabla cheques
                self.actualizar_tree(tv)
            else:
                estado_id = 0
                cliente_id = 0
                proveedor_id = 0

                if estado_desc:
                    estado_id = self.get_id_estado(estado_desc)
                else: estado_id = None

                if cliente_desc:
                    cliente_id = self.get_id_cliente(cliente_desc)
                else: cliente_id = None

                if proveedor_desc:
                    proveedor_id = self.get_id_proveedor(proveedor_desc)
                else: proveedor_id = None

                chequeDB = ChequeDB()
                cheques = chequeDB.get_cheques_by_filtros(estado_id,cliente_id,proveedor_id)
                self.actualizar_tree_busqueda(cheques,tv)
            self.limpiar_busqueda()
        except Exception as e: 
            self.mostrar_error()
            print("Error en buscar cheque ",type(e)) 




    def limpiar(self): 
        """Limpia todos los campos del alta/modificacion
        """
        self.e_fecha_ingreso.set("dd-mm-aaaa")  
        self.e_banco.set("")  
        self.e_nro_orden.set(0)  
        self.e_nro_cheque.set("")  
        self.e_importe.set(0)  
        self.e_fecha_pago.set("dd-mm-aaaa")  
        self.seleccion_cliente.set(self.desc_clientes[0])
        self.seleccion_estado.set(self.desc_estados[0])
        self.seleccion_proveedor.set("")
        self.ocultar_error()


    def limpiar_busqueda(self): 
        """Limpia todos los campos de la busqueda
        """
        self.seleccion_cliente_busqueda.set("")
        self.seleccion_estado_busqueda.set("")
        self.seleccion_proveedor_busqueda.set("")  
        self.ocultar_error()



    def obterner_datos(self,tv): 
        """llena los filtros de alta/modificacion con los datos de la fila seleccionada del treeview

        Args:
            tv (Treeview): treeview
        """
        try:
            selected_item = tv.selection()

            item_values = tv.item(selected_item, "values")
            item_id = tv.item(selected_item, "text")
            self.e_nro_orden.set(item_id)
            #columns = ('fecha_ingreso', 'cliente', 'banco','proveedor','nro_cheque','fecha_pago', 'estado', 'importe')

            self.e_fecha_ingreso.set(item_values[0])   
            self.e_banco.set(item_values[2])
            self.e_nro_cheque.set(item_values[4])
            self.e_fecha_pago.set(item_values[5])
            self.e_importe.set(item_values[7])

            self.seleccion_cliente.set(item_values[1])
            self.seleccion_proveedor.set(item_values[3])
            self.seleccion_estado.set(item_values[6])
        except Exception as e: 
            self.mostrar_error()
            print("Error en obtener datos ",type(e)) 








if __name__ == "__main__":
    
    root = tk.Tk()
    aplicacion = Vista3(root)
    root.mainloop()