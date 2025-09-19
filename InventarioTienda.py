class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"Se vendieron {cantidad} de '{nombre}'.")
                else:
                    print("No hay suficiente stock.")
                return
        print("El producto no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            print(f"\nInventario de {self.nombre_tienda}:")
            for producto in self.productos:
                print(f"- {producto['nombre']} / Precio: {producto['precio']} / Cantidad: {producto['cantidad']}")

    def producto_mas_caro(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            producto_caro = max(self.productos, key=lambda p: p["precio"])
            print(f"Producto más caro: {producto_caro['nombre']} (${producto_caro['precio']})")


# Programa principal
def main():
    tienda = InventarioTienda("Mi Tienda")

    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Producto más caro")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            tienda.agregar_producto(nombre, precio, cantidad)

        elif opcion == "2":
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            tienda.vender_producto(nombre, cantidad)

        elif opcion == "3":
            tienda.mostrar_inventario()

        elif opcion == "4":
            tienda.producto_mas_caro()

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
