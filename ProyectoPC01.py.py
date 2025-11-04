from datetime import datetime, timedelta

inventario = {
    "tenis": {"cantidad": 10, "precio": 95000},
    "bota bronco": {"cantidad": 5, "precio": 160000},
    "sandalias": {"cantidad": 8, "precio": 55000}
}

registro_mensual = []
arreglos = []


def mostrar_inventario():
    print("\nInventario actual:")
    for producto, datos in inventario.items():
        print(f"{producto.capitalize()} - Cantidad: {datos['cantidad']} - Precio: {datos['precio']}")


def registrar_venta():
    mostrar_inventario()
    producto = input("Ingrese el producto vendido: ").lower()
    cantidad = int(input("Ingrese cantidad vendida: "))

    if producto in inventario and cantidad <= inventario[producto]["cantidad"]:
        total = cantidad * inventario[producto]["precio"]
        inventario[producto]["cantidad"] -= cantidad
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        registro_mensual.append({"tipo": "venta", "producto": producto, "cantidad": cantidad, "total": total, "fecha": fecha})
        print(f"Venta registrada. Total: {total}")
    else:
        print("Producto no disponible o cantidad insuficiente.")


def registrar_ingreso():
    producto = input("Ingrese el producto nuevo o existente: ").lower()
    cantidad = int(input("Cantidad ingresada: "))
    precio = int(input("Precio unitario: "))

    if producto in inventario:
        inventario[producto]["cantidad"] += cantidad
        inventario[producto]["precio"] = precio
    else:
        inventario[producto] = {"cantidad": cantidad, "precio": precio}

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    registro_mensual.append({"tipo": "ingreso", "producto": producto, "cantidad": cantidad, "precio": precio, "fecha": fecha})
    print("Ingreso registrado correctamente.")


def registrar_arreglo():
    nombre = input("Nombre del cliente: ")
    producto = input("Tipo de calzado: ")
    descripcion = input("Descripción del arreglo: ")
    costo = int(input("Costo del arreglo: "))
    fecha_entrega = datetime.now()
    estado = "pendiente"

    arreglo = {
        "nombre": nombre,
        "producto": producto,
        "descripcion": descripcion,
        "costo": costo,
        "abonado": 0,
        "fecha_entrega": fecha_entrega,
        "estado": estado
    }

    arreglos.append(arreglo)
    registro_mensual.append({"tipo": "arreglo", "nombre": nombre, "producto": producto, "fecha": fecha_entrega.strftime("%Y-%m-%d")})
    print("Arreglo registrado exitosamente.")


def registrar_abono():
    nombre = input("Ingrese el nombre del cliente que realiza un abono: ")
    encontrado = False
    for a in arreglos:
        if a["nombre"].lower() == nombre.lower() and a["estado"] == "pendiente":
            print(f"\nArreglo de {a['producto']} - Costo total: {a['costo']} - Abonado: {a['abonado']}")
            abono = int(input("Ingrese el valor del abono: "))

            if abono <= 0:
                print("El abono debe ser un valor positivo.")
                return

            a["abonado"] += abono
            if a["abonado"] >= a["costo"]:
                a["abonado"] = a["costo"]
                a["estado"] = "pagado"
                print("El cliente ha completado el pago del arreglo.")
            else:
                print(f"Abono registrado. Total abonado: {a['abonado']} / {a['costo']}")

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
            registro_mensual.append({"tipo": "abono", "nombre": nombre, "monto": abono, "fecha": fecha})
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un arreglo pendiente con ese nombre.")


def ver_arreglos():
    print("\nLista de arreglos:")
    hoy = datetime.now()
    for a in arreglos:
        dias = (hoy - a["fecha_entrega"]).days
        estado_tiempo = "Fuera de plazo" if dias > 30 and a["estado"] == "pendiente" else "Dentro del plazo"
        print(f"\nCliente: {a['nombre']}")
        print(f"Calzado: {a['producto']}")
        print(f"Descripción: {a['descripcion']}")
        print(f"Costo: {a['costo']}")
        print(f"Abonado: {a['abonado']}")
        print(f"Saldo pendiente: {a['costo'] - a['abonado']}")
        print(f"Fecha entrega: {a['fecha_entrega'].strftime('%Y-%m-%d')}")
        print(f"Estado: {a['estado']} ({estado_tiempo})")


def marcar_retirado():
    nombre = input("Ingrese el nombre del cliente que retira el calzado: ")
    encontrado = False
    for a in arreglos:
        if a["nombre"].lower() == nombre.lower():
            if a["estado"] in ["pendiente", "pagado"]:
                a["estado"] = "retirado"
                print(f"El arreglo de {nombre} fue marcado como retirado.")
                encontrado = True
                break
    if not encontrado:
        print("No se encontró un arreglo pendiente o pagado con ese nombre.")


def generar_registro_mensual():
    print("\nRegistro mensual de actividades:")
    for r in registro_mensual:
        print(r)


def menu():
    while True:
        print("\nMENÚ CREACIONES REPISO")
        print("1. Mostrar inventario")
        print("2. Registrar venta")
        print("3. Registrar ingreso de producto")
        print("4. Registrar arreglo o remodelación")
        print("5. Ver lista de arreglos")
        print("6. Marcar calzado como retirado")
        print("7. Registrar abono de cliente")  
        print("8. Ver registro mensual")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            registrar_ingreso()
        elif opcion == "4":
            registrar_arreglo()
        elif opcion == "5":
            ver_arreglos()
        elif opcion == "6":
            marcar_retirado()
        elif opcion == "7":
            registrar_abono()
        elif opcion == "8":
            generar_registro_mensual()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


menu()
