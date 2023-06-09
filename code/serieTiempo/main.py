import os
import matplotlib.pyplot as plt

# Obtener la lista de archivos CSV en el directorio actual
path = os.path.dirname(__file__)
archivo = path+'/../BD.csv'


def validate_state(estado):
    # Leer archivo CSV y obtener la lista de lugares
    estado = estado.upper()
    estados = []

    if estado == 'NACIONAL':
        return True
    else:
        with open(archivo, 'r', encoding='utf-8') as file:
            for linea in file:
                estadoLinea = linea.strip().split(',')[2][1:-1]
                estados.append(estadoLinea)

        return estado in estados


def sub_menu():
    print("\n\t\t\t** Sistema de análisis de datos por lugar **\n")
    print('\t', ("*"*75))
    print(f'\t{" * Ingrese el nombre del lugar "}' +
          f'{"(puede ser el nombre del Estado o Nacional)":6} *', end="")
    print('\t', "")
    print('\t', ("*"*75))

    condicion = 0
    while condicion != 1:
        nombre_lugar = input(" >> ")

        if validate_state(nombre_lugar):
            obtener_datos_lugar(nombre_lugar)
            condicion = 1
            break
        else:
            print('\t', "-> Lugar inválido <-")


def obtener_datos_lugar(nombre_lugar):
    # Obtener los datos del lugar seleccionado
    matriz = []
    estadoSelect = ""
    with open(archivo, 'r', encoding='utf-8') as file:
        i = 0
        for linea in file:
            # Supongamos el formato del archivo CSV
            estadoSelect = linea.strip().split(',')[2][1:-1]
            if i == 0:
                matriz.append(linea.strip().split(',')[3:])

            if estadoSelect.upper() == nombre_lugar.upper():
                matriz.append(linea.strip().split(',')[3:])
                break
            i += 1

    lista_a = matriz[0]
    lista_b = matriz[1]
    fechas = []
    casosPorMes = []

    ultimo_mes = lista_a[0].split("-")[1]  # obtenemos el mes

    suma = 0
    indice = 0
    while (indice < len(lista_a)):
        mes_actual = lista_a[indice].split("-")[1]
        ano_actual = lista_a[indice].split("-")[2]

        if (ultimo_mes == mes_actual):
            suma += int(lista_b[indice])
        else:
            fechas.append(ultimo_mes+"-"+ano_actual)
            casosPorMes.append(suma)
            suma = 0
            indice -= 1

        if (indice+1 >= len(lista_a)):
            fechas.append(mes_actual+"-"+ano_actual)
            casosPorMes.append(suma)

        indice += 1
        ultimo_mes = mes_actual

    graphics(fechas, casosPorMes, estadoSelect)


def graphics(fechas, casosPorMes, estadoSelect):
    # Graficar la serie de datos
    fig, (ax) = plt.subplots(figsize=(12, 5))

    ax.plot(fechas, casosPorMes)
    plt.xlabel('Mes')
    plt.ylabel('Casos Confirmados')
    plt.title('Serie de datos por mes en ' + estadoSelect)
    plt.xticks(fechas, rotation=90)
    plt.grid(True)

    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)
    plt.show()


def main():
    sub_menu()


if __name__ == '__main__':
    main()
