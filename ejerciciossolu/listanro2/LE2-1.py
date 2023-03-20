# 1.Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la
# pregunta):
# - Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.
# - Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el número
# - Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad.
# Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ]
menu="""
==================================================================================================
                                        MENU
==================================================================================================

                1)Dibujar un cuadrado
                2)Identificar el múltiplo de 2
                3)Mayores de edad
"""
print(menu)
opcion=int(input("Ingrese una opción: "))
if type(opcion)==int:
    if opcion==1:#cuadrado
        lado=int(input("Ingrese tamaño del lado del cuadrado: "))
        for i in range(0,lado):
            for j in range(0,lado):
                print(" * ",end="")
            print()
            pass
    elif opcion==2:#multiplo de 2
        lista=[1,2,3,4,5,6,7,8,9,10]
        for num in lista:
            if num % 2 ==0:
                print(f"El múltiplo de 2 es: {num}")
    elif opcion==3:#mayores de edad
        listaPersonas=[["Kevin",22],["Shirly",21],["Erick",12],["Fer",24]]
        listaMayorEdad=[]
        for persona in listaPersonas:
            if(persona[1]>=18):
                listaMayorEdad.append(persona)
                print(persona[0])
        print(listaMayorEdad)
    else:
        print("Ingrese una opción válida")
else:
    print("ingrese un valor entero ,valor no permitido")