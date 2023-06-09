import casosPoblacion.main as fn2
import casosNacional.main as fn1
import serieTiempo.main as fn3


def mostrar_menu(opciones):  # Función para recorrer el diccionario
    print("\n\t\t\t\t\t\tMENÚ\n")
    print('\t\t', ("-"*60))
    print(f"\t\t{'| Seleccione la opción deseada:':61}|")
    # sorted ordena el diccionario para que las
    # opciones se muestren de manera ordenada
    for i in sorted(opciones):
        print(f'\t\t| \t{i}) {opciones[i][0]:50}|')
    print('\t\t', ("-"*60))


# Función que lee unicamente la opción ingresada por el usuario
def leer_opcion(opciones):
    while (a := input(' Opción: ')) not in opciones:
        print('>> Opción inválida\n')
    return a


# recibirá la opción seleccionada y el diccionario de opción
# ejecutará la acción correspondiente
def ejecutar(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, salida):
    opcion = None
    while opcion != salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar(opcion, opciones)
        # se imprime una línea en blanco para clarificar la salida por pantalla
        print()


def menu():
    opciones = {
        '1': ('Día con más casos a nivel nacional', funcion1),
        '2': ('% Casos confirmados de acuerdo a la población', funcion2),
        '3': ('Series de tiempo', funcion3),
        '4': ('Salir', salir)
    }
    generar_menu(opciones, '4')


def salir():
    print("Finalizando programa ...")


'''Importar los archivos que tengan el desarrollo segun la opcion'''


def funcion1():
    print('\t\tObteniendo resultados...')
    datos = fn1.read_data_base()
    resultado, estados = fn1.maximo_estados(datos)
    resultado2, fecha2, estados2 = fn1.datos_tabla(datos)
    r = fn1.transforma_datos(estados2, fecha2, resultado2)
    titulos = ['Estado', 'Fecha', 'Máximo']

    fn1.graphics(estados, resultado, r, titulos)


def funcion2():
    print('\t\tObteniendo resultados...')
    data = fn2.return_matriz()
    fn2.graphics(data[0], data[1], data[2], data[3])


def funcion3():
    fn3.sub_menu()
    print('\t\tObteniendo resultados...')


def main():
    menu()


if __name__ == '__main__':
    main()
