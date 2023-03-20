## 2.Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
## como un diccionario.
##   2.1 La biblioteca deberá tener las siguientes operaciones:
##      - Obtener la lista de categorías de libros.
##      -Obtener nombres de los libros y autores.
##      -poder cambiar el estado de un libro a prestado
##      -Lista de usuarios de la biblioteca.
biblioteca={
    "categorias":["Ciencias Sociales","Ecosistema","Ciencias Biológicas","Ciencias Jurídicas","Ciencias Contables"],
    "libros":[
        ["Historia del siglo XX 1914-1991","Hobsbawm, E. J. Eric John","disponible"],
        ["Análisis de la dinámica de las capturas de recursos marinos durante los años 1950-2014 mediante indicadores trofodinámicos","Donayre Donayre, Aida Brunela Carla", "disponible"],
        ["Caracterización bioquímica, biológica, molecular y funcional de la enzima hialuronidasa del veneno de la serpiente peruana Bothrops atrox Jergon de la Selva", "Delgadillo Arone, Julio César","disponible"],
        ["Caracterización de 21 marcadores STR autosómicos en una población peruana inmersa en un proceso judicial aplicado a la práctica forense","Delgado Ramos, Edgardo","disponible"],
        ["La contabilidad de gestión : Un enfoque de control de gestión y evaluación del desempeño, para lograr la medición integral de la gestión", "Ostengo, Héctor C.","disponible"]
    ],
    "usuarios":["Sofia","Shirly","Dayana","Fernando","Erick","Kevin"]

}
menu="""
==================================================================================================
                                    BIBLIOTECA PEDRO ZULEN
==================================================================================================

                1)Categorías de libros
                2)Nombres de libros y autores
                3)Préstamo de libro
                4)Usuarios
==================================================================================================       
"""
print(menu)
opcion=int(input("Ingrese una opción: "))
if type(opcion)==int:
    if opcion==1:#categorías
        print("Las categorías de los libros son:",biblioteca["categorias"])
    elif opcion==2:#libros y autores
        print("Los libros de la biblioteca son los siguientes: ")
        i=1
        while i <len(biblioteca["libros"]): 
            print("Titulo: ",biblioteca["libros"][i][0])
            print("Autores: ",biblioteca["libros"][i][1])
            i=i+1
    elif opcion==3:#prestamo
        libroprest=input("Ingrese el nombre del libro a realizar el préstamo: ")
        for libro in biblioteca["libros"]:
            if libroprest==libro[0]:
                libro[2]="prestamo"
                print("Libro prestado: ", libro[0])
                break
            else:
                print("Libro no encontrado")
    elif opcion==4:#usuarios
        minimenu="""
            1)Lista de usuarios
            2)Agregar nuevo usuario
        """
        print(minimenu)
        opc=int(input("Ingrese una opcion: "))
        if opc==1:
            print(biblioteca["usuarios"])
        elif opc==2:
            usuario=input("Ingrese nombre del nuevo usuario: ")
            biblioteca["usuarios"].append(usuario)
            print("Mostrando todos los usuarios...")
            print(biblioteca["usuarios"])
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción válida")
else:
    print("ingrese un valor entero ,valor no permitido")