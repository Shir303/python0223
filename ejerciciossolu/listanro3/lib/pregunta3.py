# 3.Crear un paquete de programas (módulo) que tenga las siguiente funciones
# -Una función que me permita dividir 2 números.
# -importar esos módulos desde el archivo main
def division(a, b):
    c=a/b
    return c

if __name__ == '__main__':
    
    n1=int(input("Ingresar el dividendo: "))
    n2=int(input("Ingresar el divisor: "))
    
    print(f"El cociente de dividir {n1} entre {n2} es: {division(n1,n2)}")



