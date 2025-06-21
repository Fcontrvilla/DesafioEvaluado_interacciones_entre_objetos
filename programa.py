

from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto 



def crear_tienda():  #solicita los datos para crear una tienda    
    print("\n--- Crear Nueva Tienda ---")
    nombre = input("Ingrese el nombre de la tienda: ")
    while True:
        try:
            costo_delivery = float(input("Ingrese el costo de delivery: "))
            if costo_delivery < 0:
                raise ValueError
            break
        except ValueError:
            print("Costo de delivery inválido. Por favor, ingrese un número positivo.")

    while True:
        tipo = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ").strip().lower()
        if tipo == "restaurante":
            return Restaurante(nombre, costo_delivery)
        elif tipo == "supermercado":
            return Supermercado(nombre, costo_delivery)
        elif tipo == "farmacia":
            return Farmacia(nombre, costo_delivery)
        else:
            print("Tipo de tienda no válido. Por favor, intente de nuevo.")

def ingresar_productos_a_tienda(tienda): #para ingresar productos a la tienda seleccionada
    
    while True:
        print(f"\n--- Ingresar Productos a '{tienda.get_nombre()}' ({tienda.__class__.__name__}) ---")
        nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ").strip()
        if nombre_producto.lower() == 'salir':
            break

        while True:
            try:
                precio = float(input(f"Ingrese el precio de '{nombre_producto}': "))
                if precio < 0:
                    raise ValueError
                break
            except ValueError:
                print("Precio inválido. Por favor, ingrese un número no negativo.")

        stock_input = input(f"Ingrese el stock de '{nombre_producto}' (presione Enter para stock 0): ")   #.strip()
        stock = 0
        if stock_input:
            while True:
                try:
                    stock = int(stock_input)
                    break
                except ValueError:
                    print("Stock inválido. Por favor, ingrese un número entero.")
                    stock_input = input(f"Ingrese el stock de '{nombre_producto}' (presione Enter para stock 0): ")  #.strip()
        
        tienda.ingresar_producto(nombre_producto, precio, stock)

def main():  #principal para manejo de todo
   
    tienda = crear_tienda() # Se solicita la creacion de la tienda 
    
    ingresar_productos_a_tienda(tienda) # Se solicita ingresar productos hasta que el usuario indique lo contrario 

    while True:
        print("""\n--- Opciones de la Tienda ---
         1. Listar productos
         2. Realizar venta
         3. Salir del programa
              """)
        
        opcion = input("Seleccione una opción: ")   #.strip()

        if opcion == '1':
            print(tienda.listar_productos()) # llama al método de la instancia 
        elif opcion == '2':
            print("\n--- Realizar Venta ---")
            nombre_producto = input("Ingrese el nombre del producto a vender: ").strip()
            
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad de '{nombre_producto}' a vender: "))
                    if cantidad <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Cantidad inválida. Por favor, ingrese un número entero positivo.")

            tienda.realizar_venta(nombre_producto, cantidad) # llama al método de la instancia 
            
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break # Finaliza la ejecución 
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()