# 9.en el archivo https://github.com/gianzk/python0223/blob/main/clase0503/ejercicio1.py
# agregar funcionalida para las siguientes funciones:
# -AgregarProducto
### Minisistema
roles=['admin','vendedor','inventario']

sistema={
    "nombre":"tienda",
    "usuarios":[
        {
            'name':"Shirly",
            'password':"123",
            'rol':"admin" ##vendedor ,administrador ,inventario
        }
    ],
    "sedes":[{
        "nombreSede":"Metro Colonial",
        "ubicacion":"Cercado de Lima"
    }],
    "productos":[]
}
##### funciones
## karen vera
def agregarUsuario():
    nameUsuario=input("ingrese el nombre de usuario: ")
    password=input("ingrese su password: ")
    while True:
        rol=input("ingrese su rol")
        if rol in roles:
            break
        else:
            print("ingrese un rol correcto",roles)
    
    dictUser={
        'name':nameUsuario,
        'password':password,
        'rol':rol
    }
    sistema['usuarios'].append(dictUser)
###
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar: ")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSedes():
    usuario=input("ingresa usuario: ")
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede: ")
        ubicacion=input("ingrese ubicacion: ")
        dictSede={
            'sede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")
###
def verSedes():
    print(f"Las sedes son: {sistema['sedes']}")
    pass
#####
def agregarProductos():
    usuario=input("ingresa usuario: ")
    rol=obtenerRol(usuario)
    if rol=='admin':
        product=input("Ingrese el producto: ")
        precio=float(input("ingrese el precio del producto: "))
        stock=int(input("ingrese el stock del producto: "))
        dictProduct={
            "nombre": product,
            "precio": precio,
            "stock":stock
        }
        sistema["productos"].append(dictProduct)
    else:
        print("no es un rol permitido")
    pass
#####
def cambiarStock():
    usuario=input("ingresa usuario: ")
    rol=obtenerRol(usuario)
    if rol=='admin':
        print(sistema["productos"])
        valores = input("cambiar el stock:")
        for valor in sistema["productos"]:
            valor['stock'] = valores
            print(sistema["productos"])
    pass


menu="""
    ================================================================
                        Bienvenidos a Metro!
    ================================================================ 
        1)Agregar usuario
        2)Agregar sedes
        3)Agregar productos
        4)Salir
"""
#agregarUsuario()
#print(sistema)
def main():
    print(menu)
    opcion=int(input("Seleccione una opcion: "))
    if type(opcion)==int:
        if opcion==1:#usuarios
            agregarUsuario()
            print(f"Los usuarios son: {sistema['usuarios']}")
        elif opcion==2:#sedes
            agregarSedes()
            verSedes()
        elif opcion==3:#productos
            agregarProductos()
            cambiarStock()
        elif opcion==4:
            print("Regrese pronto...")
    else:
        print("ingrese un valor entero ,valor no permitido")

main()