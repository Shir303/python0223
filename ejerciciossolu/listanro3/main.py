## 1.En el archivo main.py crear la condición __name__==’__main__’ ejecutar los demás
## problemas.
from lib.pregunta2 import Catalogo,Product
from lib.pregunta3 import division
from lib.pregunta4 import *
if __name__=='__main__':

    #pregunta 2
    catalogo = Catalogo()

    producto1 = Product("Batería ACDELCO","1000","nacional")
    producto2 = Product("TECFIL Filtro hidraulico","350","importado")
    producto3 = Product("Bujía Champion Iridium","50","importado")

    menu="""
    ==========================================================================================
                                            TOYOTA
    ==========================================================================================
    """
    print(menu)
    catalogo.agregarProducto(producto1)
    catalogo.agregarProducto(producto2)
    catalogo.agregarProducto(producto3)

    catalogo.mostrarProductos()

    #pregunta 3
    
    menu="""
    ==========================================================================================
                                        Division de 2 numeros
    ==========================================================================================
    """
    print(menu)
    n1=float(input("Ingresar el dividendo: "))
    n2=float(input("Ingresar el divisor: "))
    
    print(f"El cociente de dividir {n1} entre {n2} es: {division(n1,n2)}")

    #pregunta4
    menu="""
    ==========================================================================================
                                        PAIS-LOTE-AÑO
    ==========================================================================================
    """
    print(menu)

    producto = Producto("Motor Audi", "ARGENTINA-0015-2023")
    print(producto) 
    print(producto.identificarPais()) 
    print(producto.identificarLote()) 