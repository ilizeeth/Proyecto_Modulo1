import os
import matplotlib.pyplot as plt

# Obtener la lista de archivos CSV en el directorio actual
archivos = [archivo for archivo in os.listdir() if archivo.endswith('.csv')]


def validar_lugar(nombre_lugar):
    # Leer los archivos CSV y obtener la lista de lugares
    lugares = set()
    for archivo in archivos:
        with open(archivo, 'r') as file:
            for linea in file:
                # Supongamos que el lugar está en la primera columna
                lugar = linea.strip().split(',')[0]
                lugares.add(lugar)

    return nombre_lugar in lugares


def obtener_datos_lugar(nombre_lugar):
    while True:
        if nombre_lugar == 'Nacional' or validar_lugar(nombre_lugar):
            break
        else:
            print("Lugar inválido.")
            nombre_lugar = input(
                "Ingrese el nombre del lugar (puede ser el"
                "nombre del estado o 'Nacional'): ")

    # Obtener los datos del lugar seleccionado
    datos = []
    for archivo in archivos:
        with open(archivo, 'r') as file:
            for linea in file:
                # Supongamos el formato del archivo CSV
                lugar, fecha, casos = linea.strip().split(',')
                if lugar == nombre_lugar:
                    datos.append((fecha, int(casos)))

    # Calcular la suma de casos confirmados por mes
    casos_por_mes = {}
    for fecha, casos in datos:
        mes = fecha[3:10]  # Obtener el mes a partir del formato de fecha
        if mes in casos_por_mes:
            casos_por_mes[mes] += casos
        else:
            casos_por_mes[mes] = casos

    meses = sorted(casos_por_mes.keys())
    casos = [casos_por_mes[mes] for mes in meses]

    # Graficar la serie de datos
    plt.plot(meses, casos)
    plt.xlabel('Mes')
    plt.ylabel('Casos Confirmados')
    plt.title('Serie de datos por mes en ' + nombre_lugar)
    plt.show()


def main():
    print("Sistema de análisis de datos por lugar")
    nombre_lugar = input(
        "Ingrese el nombre del lugar "
        "(puede ser el nombre del estado o 'Nacional'): ")
    obtener_datos_lugar(nombre_lugar)


if __name__ == '__main__':
    main()
