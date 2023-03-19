## 2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el
## teclado
menu="""
=========================================================================================    
                            CALCULADORA DE AREAS
=========================================================================================    
            1)Área de círculo
            2)Área de un triangulo
            3)Área de un cuadrado
"""
pi=3.1416

print(menu)
opcion=int(input("Ingrese una opción: "))
if type(opcion)==int:
    if opcion==1:
        r=float(input("Ingrese el radio: "))
        a=pi*(r**2)
        print("El área del circulo es: ",a )
    elif opcion==2:
        b=float(input("Ingrese la base del triángulo: "))
        h=float(input("Ingrese la altura del triángulo: "))
        a=b*h/2
        print("El área del triángulo es: ",a)
    elif opcion==3:
        l=float(input("Ingrese el lado del cuadrado"))
        a=l**2
        print("El área del cuadrado es: ",a)
    else:
        print("Ingrese una opción válida")
else:
    print("ingrese un valor entero ,valor no permitido")