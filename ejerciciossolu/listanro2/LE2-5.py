## 5.Crear una funcion que al mandar como parámetro un path me liste los elementos que
## contiene esa carpeta ,en caso sea una carpeta llamar otra vez tu función que lista los
## elementos de esa subcarpeta.
import os
import pathlib

#definicion de la funcion
def my_path_function():
    print("""
==================================================================================================
        Listando directorios del path:
==================================================================================================
    """)
    with os.scandir() as ficheros:
        for fichero in ficheros:
            print(fichero.name)
my_path_function()
def ls(ruta = os.getcwd()):
    print("""
==================================================================================================
         Listando subdirectorios del path:
==================================================================================================
    """)
    listaarchivos = []
    for (_, _, archivos) in os.walk(ruta):
        listaarchivos.extend(archivos)
    return listaarchivos
print(ls())