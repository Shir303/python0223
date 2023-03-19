## 9. Defina una lista con al menos 4 elementos que a su vez sean tuplas que tengan
## la siguiente estructura ( ‘nombre’ ,’edad’, ‘dni’) y otra que sea una lista de dnis.
## -realizar un programa que filtre a la persona mayores de edad y a los que
## cumplen esa opción verificar que su dni se encuentre ahi, por ultimo imprimir
## el nombre de las personas que cumplen las condiciones anteriores
## - Definir una lista vacia , que luego se agregue el elemento que cumplio todas
## las condiciones.
listaPersonas=[("Kevin",22,"70368224"),("Shirly",21,"71265839"),("Erick",12,"76928367"),("Fer",24,"70216743")]
listaDNI=["70368224","71265839", "76928367",""]
listaMayorEdad=[]
for persona in listaPersonas:
    if(persona[1]>=18):
        if(persona[2] in listaDNI):
            listaMayorEdad.append(persona)
            print(persona[0])
print(listaMayorEdad)