## 6.Crear una funcion Main que valide el ingreso para un evento , dividir esta funcion main en
## al menos 3 sub-funciones. 
## Orquesta Sinfónica Nacional Juvenil Bicentenario: Beethoven Cinco
evento={
    'categoría': "concierto",
    'nombre':'Beethoven Cinco',
    'organizadores':"Orquesta Sinfónica Nacional Juvenil",
    'lugar':"Gran Teatro Nacional",
    'precio':[50,40,30,20,15],#Segun la platea
    'aforo':1100,
    'asistentes':700
}


def verificarEvent(event):
    if event.lower()==evento['nombre'].lower():
        return evento['nombre']
    else:
        return False

def verificarAforo():
    if evento['asistentes']<evento['aforo']:
        asientosDisponibles=evento['aforo']-evento['asistentes']
        evento['asistentes']=evento['asistentes']+1
        return asientosDisponibles
    else:
        asientosDisponibles=0
        return asientosDisponibles
def comprarEntrada():
    event=input("Ingrese el nombre del evento: ")
    if verificarEvent(event):
        print("Verificando Aforo . . .")
        if verificarAforo()>0:
            platea=int(input("Seleccionar platea (1,2,3,4,5)"))
            precioEntrada=evento['precio'][platea]
            print(f"El precio de la entrada es {precioEntrada}")
            print("Entrada comprada",verificarEvent(event))
        else:
            print("No hay aforo disponible")
    else:
        print("Nombre de evento no válido")
def verificarIngreso():
    event=input("Ingrese el nombre del evento: ")
    if verificarEvent(event):
        print("Verificando Aforo . . .")
        if verificarAforo()>0:
            lugarEvent=evento['lugar']
            print(f"Bienvenid@ al {evento['nombre']} organizado por {evento['organizadores']} realizado en {lugarEvent}")
        else:
            print("No hay aforo disponible")

def main():
    menu="""
    ==============================================================
                        BIENVENID@S A JOINNUS
    ============================================================== 
    1)Verificar Ingreso
    2)Compraer entrada
    """
    print(menu)
    opcion=int(input("Seleccione una opcion: "))
    if type(opcion)==int:
        if opcion==1:
            verificarIngreso()
        elif opcion==2:
            comprarEntrada()
        else:
            print("Ingrese una opción válida")
    else:
        print("ingrese un valor entero ,valor no permitido")

main()