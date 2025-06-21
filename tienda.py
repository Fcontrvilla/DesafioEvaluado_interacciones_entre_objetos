

from abc import ABC, abstractmethod
from producto import Producto 


class Tienda(ABC):            #clase abstracta
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = [] # Lista de objetos Producto 

    
    def get_nombre(self):
        return self.__nombre

    def get_costo_delivery(self):
        return self.__costo_delivery

    def get_productos(self):
        return self.__productos

    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock=0):
        pass # Implementación específica en cada subclase 

    @abstractmethod
    def listar_productos(self):
        pass # Implementación específica en cada subclase 

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass # Implementación específica en cada subclase 

class Restaurante(Tienda):
    tipo_tienda = "Restaurante" # atributo de clase para el tipo de tienda 

    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        print(f"Tienda Restaurante '{nombre}' creada con éxito.")

    def ingresar_producto(self, nombre, precio, stock=0):  # los productos de Restaurante siempre tienen stock 0 al crearse 
        nuevo_producto = Producto(nombre, precio, 0)
        
        
        for i, p_existente in enumerate(self.get_productos()):  # en restaurante, el stock no se modifica si se añade nuevamente 
            if p_existente == nuevo_producto:               
                print(f"Producto '{nombre}' ya existe en Restaurante.  Stock en 0.")
                return
        
        # Si no existe, se añade
        self.get_productos().append(nuevo_producto) 
        print(f"Producto '{nombre}' ingresado a '{self.get_nombre()}' (Stock siempre 0 en Restaurante).")


    def listar_productos(self):
        if not self.get_productos():  #control de error
            return "No hay productos en este restaurante."
        
        listado = f"Productos en {self.get_nombre()} ({Restaurante.tipo_tienda}):\n"
        for producto in self.get_productos():
            
            listado += f"- {producto.get_nombre()}, Precio: ${producto.get_precio()}\n" # stock no se muestra en rest.
        return listado

    def realizar_venta(self, nombre_producto, cantidad):
        
        for producto in self.get_productos():
            if producto.get_nombre().lower() == nombre_producto.lower():
                print(f"Venta de {cantidad} unidades de '{nombre_producto}' realizada en '{self.get_nombre()}'. (Stock no se valida ni modifica en Restaurante).")
                return
        print(f"Producto '{nombre_producto}' no encontrado en '{self.get_nombre()}'.")
        pass 

class Supermercado(Tienda):
    tipo_tienda = "Supermercado" 

    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        print(f"Tienda Supermercado '{nombre}' creada con éxito.")

    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, stock) 
        
        for i, p_existente in enumerate(self.get_productos()):
            
            if p_existente == nuevo_producto: # si Producto ya existe 
                
                self.get_productos()[i] = p_existente + nuevo_producto # Suma el stock 
                print(f"Stock de '{nombre}' actualizado en '{self.get_nombre()}'. Nuevo stock: {self.get_productos()[i].get_stock()}")
                return
        
        # Si no existe, lo añade
        self.get_productos().append(nuevo_producto)
        print(f"Producto '{nombre}' ingresado a '{self.get_nombre()}' con stock {nuevo_producto.get_stock()}.")

    def listar_productos(self):
        if not self.get_productos():
            return "No hay productos en este supermercado."
        
        listado = f"Productos en {self.get_nombre()} ({Supermercado.tipo_tienda}):\n"
        for producto in self.get_productos():
            stock_info = f"Stock: {producto.get_stock()}"
            if producto.get_stock() < 10: #stock bajo
                stock_info += " (Pocos productos disponibles)" 
            listado += f"- {producto.get_nombre()}, Precio: ${producto.get_precio()}, {stock_info}\n"
        return listado

    def realizar_venta(self, nombre_producto, cantidad):
        for i, producto in enumerate(self.get_productos()):
            if producto.get_nombre().lower() == nombre_producto.lower():
                if producto.get_stock() == 0: # No hay stock 
                    print(f"No hay stock de '{nombre_producto}' en '{self.get_nombre()}'.")
                    return
                
                # vender solo la cantidad disponible 
                cantidad_a_vender = min(cantidad, producto.get_stock())
                
                nuevo_stock = producto.get_stock() - cantidad_a_vender
                producto.set_stock(nuevo_stock) # colaboracion uso de setter de Producto
                print(f"Venta de {cantidad_a_vender} unidades de '{nombre_producto}' realizada en '{self.get_nombre()}'. Stock restante: {producto.get_stock()}")
                return
        print(f"Producto '{nombre_producto}' no encontrado en '{self.get_nombre()}'.")
        

class Farmacia(Tienda):
    tipo_tienda = "Farmacia" 

    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)
        print(f"Tienda Farmacia '{nombre}' creada con éxito.")

    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, stock) # Stock se respeta para Farmacia
        
        for i, p_existente in enumerate(self.get_productos()):
            if p_existente == nuevo_producto: # Producto existe 
                self.get_productos()[i] = p_existente + nuevo_producto # Suma el stock 
                print(f"Stock de '{nombre}' actualizado en '{self.get_nombre()}'. Nuevo stock: {self.get_productos()[i].get_stock()}")
                return
        
        self.get_productos().append(nuevo_producto)
        print(f"Producto '{nombre}' ingresado a '{self.get_nombre()}' con stock {nuevo_producto.get_stock()}.")

    def listar_productos(self):
        if not self.get_productos():
            return "No hay productos en esta farmacia."
        
        listado = f"Productos en {self.get_nombre()} ({Farmacia.tipo_tienda}):\n"
        for producto in self.get_productos():
            precio_info = f"Precio: ${producto.get_precio():.2f}"
            if producto.get_precio() > 15000: # Mensaje de envío gratis 
                precio_info += " (Envío gratis al solicitar este producto)"
            # Ocultar stock para Farmacia 
            listado += f"- {producto.get_nombre()}, {precio_info}\n"
        return listado

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3: # Validación de cantidad máxima por venta en Farmacia 
            print(f"En Farmacia, no se puede solicitar una cantidad superior a 3 por producto. Venta de '{nombre_producto}' no realizada.")
            return

        for i, producto in enumerate(self.get_productos()):
            if producto.get_nombre().lower() == nombre_producto.lower():
                if producto.get_stock() == 0: # No hay stock 
                    print(f"No hay stock de '{nombre_producto}' en '{self.get_nombre()}'.")
                    return
                
                cantidad_a_vender = min(cantidad, producto.get_stock())
                
                nuevo_stock = producto.get_stock() - cantidad_a_vender
                producto.set_stock(nuevo_stock) # Colaboracion: Uso de setter de Producto
                print(f"Venta de {cantidad_a_vender} unidades de '{nombre_producto}' realizada en '{self.get_nombre()}'. Stock restante: {producto.get_stock()}")
                return
        print(f"Producto '{nombre_producto}' no encontrado en '{self.get_nombre()}'.")
      