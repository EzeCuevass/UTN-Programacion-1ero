# # Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se
# # debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase
# # e implementarla.

# class Libro:
#     # Constructor
#     def __init__(self,titulo:str,autor:str,publicacion:int):
#         self.__titulo = titulo
#         self.__autor = autor
#         self.__publicacion = publicacion
#     # Metodos
#     def MostrarLibro(self):
#         print("Titulo del libro:", self.__titulo)
#         print("Autor del libro: ", self.__autor)
#         print("Año de publicacion del libro: ", self.__publicacion)

# datos_libro = Libro("El Diario de Ana Frank", "Ana Frank", 1947)
# datos_libro.MostrarLibro()
# # print(datos_libro.__titulo)

# Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe
# poder calcular el área y el perímetro. Se debe crear la clase e implementarla.

# class Rectangulo:
#     def __init__(self,base:int,altura:int):
#         self.__base = base
#         self.__altura = altura
    
#     def area(self):
#         base = self.__base 
#         altura = self.__altura
#         area = base*altura
#         print(f"El area del rectangulo es {area}")
#     def perimetro(self):
#         base = self.__base 
#         altura = self.__altura
#         perimetro = (base*2) + (altura*2)
#         print(f"El perimetro del rectangulo es {perimetro}")

# rectangulo1 = Rectangulo(8,6)
# rectangulo1.area()
# rectangulo1.perimetro()


# Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. Se debe
# crear la clase e implementarla.

# class Calculadora:
#     def __init__(self,operacion:str,numero1:int,numero2:int):
#         self.operacion = operacion
#         self.numero1 = numero1
#         self.numero2 = numero2
    
#     def suma(self):
#         suma = self.numero1 + self.numero2
#         return suma
    
#     def resta(self):
#         resta = self.numero1 - self.numero2
#         return resta

#     def multiplicacion(self):
#         multiplicacion = self.numero1 * self.numero2
#         return multiplicacion
    
#     def division(self):
#         division = self.numero1 / self.numero2
#         return division

#     def valor_operacion(self):
#         match self.operacion:
#             case "+":
#                 print(f"El resultado de la suma es: {self.suma()}")
#             case "-":
#                 print(f"El resultado de la resta es: {self.resta()}")
#             case "*":
#                 print(f"El resultado de la multiplicacion es: {self.multiplicacion()}")
#             case "/":
#                 print(f"El resultado de la division es: {self.division()}")

# calcu = Calculadora("/", 7, 8)
# calcu.valor_operacion()


# Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal
# las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las
# características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que
# realizan. Se debe crear la clase e implementarla.

class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

class Perro:
    def __init__(self):
        super(Animal)
    
    def sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def __init__(self):
        super().__init__(self)
        self.nombre = self.nombre

    def sonido(self):
        print(self)

gato = Gato("Roberto")

gato.sonido()