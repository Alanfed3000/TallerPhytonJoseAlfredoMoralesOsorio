def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))

    for producto in inventario:
        if producto[0] == nombre:
            producto[1] += cantidad
            print(f"Se han agregado {cantidad} unidades a {nombre}.")
            return
    inventario.append([nombre, cantidad])
    print(f"Se ha agregado {nombre} al inventario.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    productos_unicos = {}
    for producto in inventario:
        nombre, cantidad = producto
        if nombre in productos_unicos:
            productos_unicos[nombre] += cantidad
        else:
            productos_unicos[nombre] = cantidad

    print("\nInventario:")
    for nombre, cantidad in productos_unicos.items():
        print(f"{nombre}: {cantidad}")

def vender_producto(inventario):
    nombre = input("Nombre del producto a vender: ")
    cantidad_venta = int(input("Cantidad a vender: "))

    for producto in inventario:
        if producto[0] == nombre:
            if producto[1] >= cantidad_venta:
                producto[1] -= cantidad_venta
                print(f"Se han vendido {cantidad_venta} unidades de {nombre}.")
                if producto[1] == 0:
                    inventario.remove(producto)
                return
            else:
                print(f"No hay suficiente stock de {nombre}.")
                return
    print(f"No se encontró {nombre} en el inventario.")

def main():
    inventario = []
    while True:
        print("\n=== Inventario Básico ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            vender_producto(inventario)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()