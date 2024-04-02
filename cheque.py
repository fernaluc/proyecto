from estado import *
from cliente import *
from proveedor import *

class Cheque:
                #      int, date,         Cliente , str  , Proveedor, int    , date      ,Estado, float
    def __init__(self, id, fecha_ingreso, cliente, banco,proveedor,nro_cheque,fecha_pago, estado, importe):
        self._id = id
        self._fecha_ingreso = fecha_ingreso
        self._banco = banco
        self._nro_cheque = nro_cheque
        self._estado = estado
        self._cliente = cliente
        self._proveedor = proveedor
        self._fecha_pago = fecha_pago
        self._importe = importe



    #getter
    @property
    def id(self): return self._id
       
    #setter 
    @id.setter 
    def id(self, id): self._id = id 

    #getter
    @property
    def fecha_ingreso(self): return self._fecha_ingreso
       
    #setter 
    @fecha_ingreso.setter 
    def fecha_ingreso(self, fecha_ingreso): self._fecha_ingreso = fecha_ingreso 

    #getter
    @property
    def banco(self): return self._banco
       
    #setter 
    @banco.setter 
    def banco(self, banco): self._banco = banco

    #getter
    @property
    def nro_cheque(self): return self._nro_cheque
       
    #setter 
    @nro_cheque.setter 
    def nro_cheque(self, nro_cheque): self._nro_cheque = nro_cheque

    #getter
    @property
    def estado(self): return self._estado
       
    #setter 
    @estado.setter 
    def estado(self, estado): self._estado = estado

    #getter
    @property
    def cliente(self): return self._cliente
       
    #setter 
    @cliente.setter 
    def cliente(self, cliente): self._cliente = cliente

    #getter
    @property
    def proveedor(self): return self._proveedor
       
    #setter 
    @proveedor.setter 
    def proveedor(self, proveedor): self._proveedor = proveedor
    
    #getter
    @property
    def fecha_pago(self): return self._fecha_pago
       
    #setter 
    @fecha_pago.setter 
    def fecha_pago(self, fecha_pago): self._fecha_pago = fecha_pago
 
    #getter
    @property
    def importe(self): return self._importe
       
    #setter 
    @importe.setter 
    def importe(self, importe): self._importe = importe


    def ver_cheque(self):
        print("id "+str(self._id))
        print("fecha ingreso "+self._fecha_ingreso)
        print("banco  "+self._banco)
        print("nro cheque "+self._nro_cheque)
        print("estado "+self._estado.descripcion)
        print("cliente "+self._cliente.descripcion)
        if self._proveedor is not None:  print("proveedor "+self._proveedor.descripcion)
        else: print("no hay proveedor")
        print("fecha pago "+self._fecha_pago)
        print("importe "+ str(self._importe))
        print("fin")
       