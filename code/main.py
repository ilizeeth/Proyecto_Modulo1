def mostrar_menu(opciones): #Función para recorrer el diccionario
    print("\n\t\t\t\t\t\tMENÚ\n")
    print('\t\t',("-"*60))
    print(f"\t\t{'| Seleccione la opción deseada:':61}|")
    for i in sorted(opciones): #sorted ordena el diccionario para que las opciones se muestren de manera ordenada
        print(f'\t\t| \t{i}) {opciones[i][0]:50}|')
    print('\t\t',("-"*60))

def leer_opcion(opciones): #Función que lee unicamente la opción ingresada por el usuario
    while (a := input(' Opción: ')) not in opciones:
        print('>> Opción inválida\n')
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
   opciones={
   '1':('Día con más casos a nivel nacional',funcion1),
   '2':('% Casos confirmados de acuerdo a la población',funcion2),
   '3':('Series de tiempo',funcion3),
   '4':('Salir',salir)
   }
   generar_menu(opciones,'4')

def salir():
    print("Ha salido del programa")

########## Importar los archivos que tengan el desarrollo segun la opcion ##########
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