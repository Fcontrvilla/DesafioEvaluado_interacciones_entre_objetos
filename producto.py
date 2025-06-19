

class Producto:   
    def __init__(self, nombre, precio, stock=0):
       
        self.__nombre = nombre  #privado  Encapsulamineto
        self.__precio = precio  #privado
        self.__stock = self.validar_stock(stock) # Validamos el stock al inicio

    def validar_stock(self, stock):  # stock nunca menor que 0
       return max(0, stock)  #si stock es menor que 0 asigna 0

    # Getters accede a los atributos privados __xxx
    def get_nombre(self): 
        return self.__nombre

    def get_precio(self): # Getters accede a los atributos
        return self.__precio

    def get_stock(self): # Getters accede a los atributos
        return self.__stock

    # Setter 
    def set_stock(self, nuevo_stock):
        self.__stock = self.validar_stock(nuevo_stock)

   
    def __eq__(self, other):   # Compara si dos productos son iguales segun nombre   ---sobrecarga
        
        if isinstance(other, Producto):  #función integrada que verifica si un objeto es una instancia de una clase específica o de una subclase de esta
            return self.__nombre.lower() == other.get_nombre().lower()
        return False

    def __add__(self, other):  #suma stocks de productos con el mismo nombre. ----sobrecarga
        
        if isinstance(other, Producto) and self.__eq__(other):
            # Conserva el precio del primer ingreso
            return Producto(self.__nombre, self.__precio, self.__stock + other.get_stock()) #conserva nombre y precio, suma stock
        raise TypeError("Solo se pueden sumar productos con el mismo nombre.")

    
    
    
    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: ${self.__precio}, Stock: {self.__stock}"