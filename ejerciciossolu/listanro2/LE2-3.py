## 3. Definir una función que retorne el mayor valor al ingresar 2 números.
print("""
==================================================================================================
                                El numero mayor
==================================================================================================
""")
num1=float(input("Ingrese el primero numero a comparar: "))
num2=float(input("Ingrese el segundo numero a comparar: "))
def comparandoNum(num1,num2):
    if(num1==num2):
        resultado="Los números son iguales, el mayor es el mismo numero: "
        print(resultado,num1)
    elif(num1!=num2):
        if(num1>num2):
            result="El primer número es mayor que el segundo: "
            print(result, num1)
        else:
            result="El segundo numero es mayor que el primero: "
            print(result, num2)

comparandoNum(num1,num2)