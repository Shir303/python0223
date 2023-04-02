# 5. para la pregunta 4 al importar la funciones usar el manejo de errores (try ,except) y en las
# sentencias de “ else “ imprimir la ruta del directorio de trabajo os.getcwd() y en la sentencia
# finally imprimir “proceso terminado”
from pregunta3 import division
import os

while(True):
    try:
        n1=float(input("Ingresar el dividendo: "))
        n2=float(input("Ingresar el divisor: "))

        print(f"El cociente de dividir {n1} entre {n2} es: {division(n1,n2)}")

        
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        print(os.getcwd())
        break 
    finally:
        print("Proceso terminado") 