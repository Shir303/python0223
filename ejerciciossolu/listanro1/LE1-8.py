## 8.Escribir un programa que almacene la cadena de caracteres contraseña en una
## variable, pregunte al usuario por la contraseña e imprima por pantalla si la
## contraseña introducida por el usuario coincide con la guardada en la variable sin
## tener en cuenta mayúsculas y minúsculas.

contraseña="contraseña"
print("Bienvenid@")
password=input("Ingresa la contraseña para acceder al sistema: ")
if contraseña==password.lower():
    print("""Contraseña correcta
    Ingresó correctamente""")
else:
    print("""Contraseña incorrecta
    Vuelva a intentarlo""")

