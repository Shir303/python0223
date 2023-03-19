## 7. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
## ● Si los dos números son iguales
## ● Si los dos números son diferentes
## ● Si el primero es mayor que el segundo
## ● Si el segundo es mayor o igual que el primero
print("Comparación de números")
num1=int(input("Ingrese el primero numero a comparar: "))
num2=int(input("Ingrese el segundo numero a comparar: "))
if(num1==num2):
    resultado="Los números son iguales"
    print(resultado)
elif(num1!=num2):
    resultado="Los números son diferentes"
    print(resultado)
    if(num1>num2):
        result="El primer número es mayor que el segundo"
        print(result)
    else:
        result="El segundo numero es mayor que el primero"
        print(result)
