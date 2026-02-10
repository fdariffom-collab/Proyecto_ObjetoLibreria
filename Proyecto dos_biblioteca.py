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
            if nomLibro in self.registroPrestamo.keys():
                print(f'Lo sentimos, ese libro ha sido prestado a {self.registroPrestamo[nomLibro]}. No se encuentra disponible.  ')
            else:
                self.registroPrestamo.update({nomLibro:nomCliente})
                print(f'Gracias {nomCliente} por usar nuestra biblioteca. Prestamo exitoso. ')
                #La siguiente parte de este bloque es una de las sugerencias de mejoras de codigo
                #La idea es generar una base de datos para los libros en prestamo
                archivoPrestamo=open('detallesPrestamos.txt','w')#Crea o sobrescribe el archivo de texto como base de datos.
                for i in self.registroPrestamo.items():
                    titulo=i[0]
                    cliente=i[1]
                    archivoPrestamo.write(titulo)
                    archivoPrestamo.write(' ')
                    archivoPrestamo.write(cliente)
                    archivoPrestamo.write('\n')
                archivoPrestamo.close()
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

    #Este metodo es para obtener una lista de los libros prestados y los usuarios que los solicitaron
    #Es parte de las mejoras sugeridas para el proyecto.
    def listaPrestamo(self):
        for libro in self.registroPrestamo.items():
            print(libro)
        
    #Metodo de eliminacion de libro de la base de datos y del codigo: Mejoras sugeridas en el proyecto
    def eliminarLibro(self,nomLibro):
        if nomLibro in self.listaLibros:
            self.listaLibros.remove(nomLibro)
            print('Libro eliminado con éxito. La base de datos ha sido actualizada.')
            actdatos=open(archivoBase,'w')
            for libro in self.listaLibros:
                actdatos.write(libro)
                actdatos.write('\n')
            actdatos.close()
        else:
            print('Lo sentimos, ese libro no se encuentra en nuestras existencias.')
            

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
        5. Ver la lista de libros prestados por usuario
        6. Eliminar un Libro
        """)
        user_elec=str(input('Elige C para continuar o X para cancelar: ')).upper()
        if user_elec=="C":
            user_elec2=int(input('Por favor, ingrese una opción de la 1 a la 6 de las enlistadas: '))

            if user_elec2==1:
                objLibreria.verLista()

            elif user_elec2==2:
                nomCliente=str(input('Ingrese el nombre del solicitante: '))
                nomLibro=input('Ingrese el título del libro que desea solicitar para préstamo: ')
                objLibreria.prestarLibro(nomLibro,nomCliente)
            
            elif user_elec2==3:
                print('Para añadir un libro ingrese el nombre del ejemplar: ')
                nomLibro=str(input('Título: '))
                objLibreria.addLibro(nomLibro)
            
            elif user_elec2==4:
                print('Para devolver un libro, ingrese el nombre del ejemplar: ')
                nomLibro=str(input('Título: '))
                objLibreria.devolverLibro(nomLibro)

            elif user_elec2==5:
                print('A continuación los libros que se encuentran en préstamo con el nombre del usuario que los ha solicitado: ')
                objLibreria.listaPrestamo()

            elif user_elec2==6:
                print('Para eliminar un libro, ingrese el nombre del ejemplar:')
                nomLibro=str(input('Título: '))
                objLibreria.eliminarLibro(nomLibro)

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
    archivolibros.close()
#La creacion del objeto libreria
objLibreria=Library(nombreLibrary,listaLibros)
main()
#A continuacion las mejoras que se proponen para el codigo:
#Implementar base de datos (al igual que la listas de libros) para los libros prestados
#Hecho
#Agregar un metodo para que devuelva el registro de todos los libros prestados con el nombre de la persona que los solicito
#Hecho
#Implementar un metodo para eliminar un libro
#Hecho
#Me falta modificar el bloque de codigo para devolver un libro y sobrescribir la base de datos de libros prestados
#Y donde se creo ese archivo?
#Arreglar el archivo .txt de la lista de libros porque no me reconoce los libros al solicitar el prestamo, solo reconoce el ultimo libro de la lista.
#Poner condicion para no eliminar un libro si es que este se encuentra prestado
