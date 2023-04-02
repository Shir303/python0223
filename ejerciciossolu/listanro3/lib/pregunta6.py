# 6.el siguiente archivo
# https://github.com/gianzk/python0223/blob/main/clase1203/ejercicioopp.py
# se necesita agregar quitar producto del carrito ,mostrar precio total del carrito.
class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} con ID de {self.id} cuesta {self.precio} y tiene un stock de {self.stock} unidades."
    def updateStock(self,stock):
        self.stock=stock
    
class CarritoCompra:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProdcut(self,id):
        for product in self.listaProductos:
            if product.id == int(id):
                self.listaProductos.remove(product)
                product.updateStock(product.stock + 1)
                print("Producto eliminado con éxito")
                break
        else:
            print("No se encontró este producto en el carrito.")
        pass
    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print(len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Quitar Producto
    4)Mostrar precio total
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del producto:")
            stock=int(input("ingrese el stock del producto:"))
            release=int(input("ingrese el release del producto:"))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto(px)
        except Exception as Error:
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        id_producto = int(input("Ingrese el ID del producto a quitar: "))
        carrito.quitarProdcut(id)
    
    if opcion==4:
        carrito.calcularPrecio()
        print(f"El precio total es: {carrito.precioTotal}")

    if opcion==5:
        print("Vuelva pronto...")
        break