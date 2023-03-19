## 10.Defina un diccionario que tenga las siguientes llaves (nombre de curso,cantidad
## de alumnos,activo(tipo boleano),nombre de profesor,max nota,alumnos(lista)) a
## todos ellos como valor que lleven un valor de inicializacion ,por ejemplo si es entero
## 0 ,si es string una cadena vacia.
## -Realizar al menos 3 inputs para ingresar por teclado nuevos valores para el diccionario .
## -Imprimir el diccionario.
print("Registrando un curso..................................................................")
curso={
    "Curso":"",
    "CantidadAlumnos":0,
    "Activo":False,
    "Profesor":"",
    "MaxNota":0,
    "Alumnos":[],
}
cursoNombre=input("Ingrese el nombre de curso: ")
curso['Curso']=cursoNombre
cantidadAlum=int(input("Ingrese la cantidad de alumnos del curso: "))
curso['CantidadAlumnos']=cantidadAlum
estado=bool(input("Ingrese el estado del curso (True/False): "))
curso['Activo']=estado
profesor=input("Ingrese el nombre del profesor del curso: ")
curso['Profesor']=profesor
maxnota=int(input("Ingrese la nota máxima del curso: "))
curso['MaxNota']=maxnota
i=1
while i<=cantidadAlum:
    alumno=input("ingrese el nombre de alumno: ")
    curso['Alumnos'].append(alumno)
    i=i+1
print(curso)

