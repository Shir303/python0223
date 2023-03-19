## 1.Realizar un programa que ingrese sus datos personales e imprimirlos, poner en
## comentario su nombre completo.
##Nombre y Apellidos: Shirly Dayana Barzola Brusil
mensajeI="-----------------------BIENVENID@! ingresa los siguientes datos-----------------------"
print(mensajeI)
nombre=input("Ingresa tus nombres: ")
apellido= input("Ingresa tus apellidos: ")
edad=int(input("Ingresa tu edad: "))
dni=input("Ingresa tu DNI: ")
mensajeF="""**************************************************************************************
Gracias por completar el formulario
Los datos ingresados son los siguientes: """
print(mensajeF)
print(nombre)
print(apellido)
print(edad)
print(dni)
