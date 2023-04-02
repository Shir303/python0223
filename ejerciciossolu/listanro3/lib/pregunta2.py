# 2. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
# clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
# tener un método para agregar productos y otra para mostrar toda la lista de productos.
class Catalogo:

    def __init__(self):
         self.productos = []

    def agregarProducto(self,producto):
         self.productos.append(producto)

    def mostrarProductos(self):
         for producto in self.productos:
            print(producto)     


class Product:
     
     def __init__(self,nombre,precio,categoria):
          self.nombre = nombre
          self.precio = precio
          self.categoria = categoria

     def __str__(self) -> str:
          return f"La autoparte {self.nombre} cuesta S/{self.precio} y su categoría es {self.categoria}"
     


if __name__ == '__main__':
     catalogo = Catalogo()

     producto1 = Product("Batería ACDELCO","1000","nacional")
     producto2 = Product("TECFIL Filtro hidraulico","350","importado")
     producto3 = Product("Bujía Champion Iridium","50","importado")


     catalogo.agregarProducto(producto1)
     catalogo.agregarProducto(producto2)
     catalogo.agregarProducto(producto3)

     catalogo.mostrarProductos()