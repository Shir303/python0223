## 3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división
## y división entera.

menu="""
=========================================================================================    
                                CALCULADORA
=========================================================================================
            1)Suma
            2)Resta
            3)Multiplicación
            4)División
            5)División entera
    Nota: Se usarán 3 números en el orden ingresado para el cálculo de la operación
"""

print(menu)
opcion=int(input("Ingrese una opción: "))
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))


if type(opcion)==int:
    if opcion==1:#suma
        resultado=num1+num2+num3
        print("El resultado de la suma es: ",resultado)
    elif opcion==2:#resta
        resultado=num1-num2-num3
        print("El resultado de la resta es: ",resultado)
    elif opcion==3:#multiplicacion
        resultado=num1*num2*num3
        print("El resultado de la multiplicación es: ",resultado)
    elif opcion==4:#división
        if num2==0:
            print("Los divisores no pueden ser 0")
        elif num3==0:
            print("Los divisores no pueden ser 0")
        else:
            resultado=num1/num2/num3
            print("El resultado de la división es: ",resultado)

    elif opcion==5:#división entera
        if num2==0:
            print("Los divisores no pueden ser 0")
        elif num3==0:
            print("Los divisores no pueden ser 0")
        else:
            resultado=num1//num2//num3
            print("El resultado de la división entera es: ",resultado)
    else:
        print("Ingrese una opción válida")
else:
    print("ingrese un valor entero ,valor no permitido")