# Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se
# debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase
# e implementarla.

class Libro:
    # Constructor
    def __init__(self,titulo:str,autor:str,publicacion:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicacion = publicacion
    # Metodos
    def MostrarLibro(self):
        print("Titulo del libro:", self.__titulo)
        print("Autor del libro: ", self.__autor)
        print("Año de publicacion del libro: ", self.__publicacion)

datos_libro = Libro("El Diario de Ana Frank", "Ana Frank", 1947)
datos_libro.MostrarLibro()
# print(datos_libro.__titulo)