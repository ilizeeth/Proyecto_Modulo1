#Archivo prueba para verificar que el repositorio funciona de manera correcta

def mostrar_menu(opciones): #Función para recorrer el diccionario
    print('Seleccione la opción deseada:')
    for i in sorted(opciones): #sorted ordena el diccionario para que las opciones se muestren de manera ordenada
        print(f' {i}) {opciones[i][0]}')

def leer_opcion(opciones): #Función que lee unicamente la opción ingresada por el usuario
    while (a := input(' Opción: ')) not in opciones:
        print('Opción inválida')
    return a

def ejecutar(opcion, opciones): #recibirá la opción seleccionada y el diccionario de opción  ejecutará la acción correspondiente
    opciones[opcion][1]()

def generar_menu(opciones,salida):
    opcion =None
    while opcion!=salida:
        mostrar_menu(opciones)
        opcion=leer_opcion(opciones)
        ejecutar(opcion,opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def menu():
   print("\n\t\tMENÚ\n")
   opciones={
   '1':('Día con más casos a nivel nacional',funcion1),
   '2':('% Casos confirmados de acuerdo a la población',funcion2),
   '3':('Series de tiempo',funcion3),
   '4':('Salir',salir)
   }
   generar_menu(opciones,'4')

def salir():
    print("Ha salido del programa")
def funcion1():
    pass
def funcion2():
    pass
def funcion3():
    pass

def main():
    menu()


if __name__ == '__main__':
    main()