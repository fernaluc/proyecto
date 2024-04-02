import re

class Validacion_campos():
        
        patron_fecha = r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])[/|-](0[1-9]|1[0-2])[/|-]\d{4}"

        def __init__(self): 
            pass



        @classmethod    
        def es_error_fecha(cls, fecha):
            """Funcion que verifica si la fecha pasada como paramtro esta en estado incorrecto

            Args:
                fecha (str): fecha a verificar

            Returns:
                bool: retorna false si la fecha no tiene error o true si la fecha esta incorrecta
            """
            if re.match(cls.patron_fecha, fecha):    
                return False
            else:
                return True
