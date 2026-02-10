class Library:
    def __init__(self,nombreLibrary,listaLibros):
        self.nombreLibrary=nombreLibrary
        self.listaLibros=listaLibros
        self.registroPrestamo={}#Diccionario con nomLibro:nomCliente para prestamos
        
#Definiendo metodos
    def verLista(self):
        print(f'En {self.nombreLibrary} tenemos los siguientes libros disponibles: ')
        for libro in self.listaLibros:
            print(libro)
    
    def prestarLibro(self,nomLibro,nomCliente):
        if nomLibro in self.listaLibros:
            if nomLibro not in self.registroPrestamo.keys():
                self.registroPrestamo.update({nomLibro:nomCliente})
                print(f'Gracias {nomCliente} por usar nuestra biblioteca. Prestamo exitoso. ')
            else:
                print(f'Lo sentimos, ese libro ha sido prestado a {self.registroPrestamo[nomLibro]}. No se encuentra disponible.  ')
        else:
            print(f'¡Ups! {nomLibro} no está en nuestros registros. Intenta otra opción. ')


    def addLibro(self,nomLibro):
        if nomLibro in self.listaLibros:
            print(f'Lo siento, {nomLibro} ya ha sido agregado. ')
        else:
            self.listaLibros.append(nomLibro)
            totLibros=open(archivoBase,'a')
            totLibros.write('\n')
            totLibros.write(nomLibro)
            totLibros.close()
            print(f'{nomLibro} ha sido agregado a nuestra colección y se ha actualizado nuestra información. Gracias')
            

    def devolverLibro(self,nomLibro):
        if nomLibro in self.registroPrestamo.keys():
            print(f'Hola {self.registroPrestamo.get(nomLibro)}! Gracias por la devolución del libro {nomLibro}.')
            self.registroPrestamo.pop(nomLibro)
        else:
            print('Ups, parece haber un error. Ese libro no puede ser devuelto.')

#Ahora el desarrollo del menu
def main():
    control=True
    while control==True:
        print(f'Biblioteca {nombreLibrary}')
        print("""Menú Principal:
        1. Ver la lista de libros de nuestra biblioteca
        2. Solicitar préstamo
        3. Añadir un libro
        4. Devolver un Libro
        """)
        user_elec=str(input('Elige C para continuar o X para cancelar: ')).upper()
        if user_elec=="C":
            user_elec2=int(input('Por favor, ingrese una opción de la 1 a la 4 de las enlistadas: '))

            if user_elec2==1:
                print('Los libros de nuestra biblioteca son: ')
                objLibreria.verLista()

            elif user_elec2==2:
                nomCliente=str(input('Ingrese el nombre del solicitante: '))
                nomLibro=str(input('Ingrese el título del libro que desea solicitar para préstamo: '))
                objLibreria.prestarLibro(nomLibro,nomCliente)
            
            elif user_elec2==3:
                print('Para añadir un libro ingrese el nombre del ejemplar: ')
                nomLibro=str(input('Título: '))
                objLibreria.addLibro(nomLibro)
            
            elif user_elec2==4:
                print('Para devolver un libro, ingrese el nombre del ejemplar: ')
                nomLibro=str(input('Título: '))
                objLibreria.devolverLibro(nomLibro)
            else:
                print('Por favor, elija una opción válida .')
        elif user_elec=="X":
            control=False
        else:
            print('No es una opción válida. ')

#Por ultimo , la creacion del objeto libreria y el inicio del programa
if __name__=='__main__':
    listaLibros=[]
    nombreLibrary=str(input('Ingresa el nombre de la biblioteca: '))
    archivoBase=str(input('Ingresa el nombre de tu archivo de texto con la extensión de archivo .txt : '))
    archivolibros=open(archivoBase,"r")
    for libro in archivolibros:
        listaLibros.append(libro)
#La creacion del objeto libreria
objLibreria=Library(nombreLibrary,listaLibros)
main()
#A continuacion las mejoras que se proponen para el codigo:
#Implementar base de datos (al igual que la listas de libros) para los libros prestados
#Agregar metodo para que devuelva el registro de todos los libros prestados con el nombre de la persona de quien ha solicitado el prestamo
#Implementar un metodo para eliminar un libro