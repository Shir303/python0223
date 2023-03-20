## 4. Definir una función que imprima los argumentos ingresados desde línea de comandos
## Nota: Usar import sys.argv => *args
import sys

variable=sys.argv
#definicion de la funcion
def my_path_function(*args):
    print("""
==================================================================================================
        Args:
==================================================================================================
    """)
    print(args)
    print(type(args))
#Llamado a la funcion
my_path_function(variable)