# 7.el siguiente texto : “ Lorem Ipsum es simplemente el texto de relleno de las imprentas y
# archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el
# año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó
# una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
# No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos 
# electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la 
# creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más
# recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye
# versiones de Lorem Ipsum.”
# realizar al menos 3 funciones de string al texto de arriba.
lorem= "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas Letraset, las cuales contenian pasajes de Lorem Ipsum, y más  recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."
menu="""
    ==============================================================
                        OPERACIONES CON STRING
    ============================================================== 
    1)Longitud del texto
    2)Encuentra tu palabra
    3)Reemplazando
    4)Cortando el mensaje
"""
def longitud():
    return len(lorem)
def searchWord(word):
    encontrado=lorem.lower().find(word)
    if(encontrado>-1):
        print(f"Tu palabra ha sido encontrada en el caracter numero {encontrado}")
    else:
        print("Tu palabra no se encuentra en el texto")
def replaceWord(letra,palabra):
    newLorem=lorem.replace(letra,palabra)
    return newLorem
def cortarMessage(posI, posF):
    newLorem=lorem[posI:posF]
    return newLorem

def main():
    print(menu)
    opcion=int(input("Seleccione una opcion: "))
    if type(opcion)==int:
        if opcion==1:
            print(f"La longitud del texto es {longitud()}")
        elif opcion==2:
            word=input("Ingrese su palabra a buscar: ")
            searchWord(word)
        elif opcion==3:
            letra=input("Ingrese su palabra a reemplazar: ")
            palabra=input("Ingrese el texto por el cual se reemplazará: ")
            print(f"El nuevo texto es: {replaceWord(letra,palabra)}")
        elif opcion==4:
            posI=int(input("Ingrese la posicion inicial de corte: "))
            posF=int(input("Ingrese la posicion final de corte: "))
            print(f"El nuevo texto es: {cortarMessage(posI,posF)}")
    else:
        print("ingrese un valor entero ,valor no permitido")

main()