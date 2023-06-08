import os
from matplotlib import pyplot as plt


def read_data_base():
    path = os.path.dirname(__file__)
    with open(path+'/../BD.csv', 'r', encoding='utf-8') as f:
        linea = True
        matriz = []
        while linea:
            linea = f.readline()
            # Limpieza de datos si ya no hay cosas en una linea
            if len(linea) > 0:
                fila = linea.split(',')
                matriz.append(fila)
    return matriz


def return_matriz():
    matriz = read_data_base()

    poblacion = []
    estado = []
    contagios = []
    porcentaje = []

    for i in range(1, len(matriz)):
        fila = matriz[i]
        estado.append(fila[2][1:-1])
        poblacion.append(int(fila[1]))
        sum = 0
        porc = 0
        for j in range(3, len(fila)):
            cantidad = fila[j]
            sum += int(cantidad)
        porc = (int(fila[1])*100)/sum
        porcentaje.append(round(porc, 2))
        contagios.append(sum)

    return estado, poblacion, contagios, porcentaje


def show_tabla(estados, poblacion, contagios, porcentaje):
    data = []
    for i in range(len(estados)):
        row = [estados[i], poblacion[i], contagios[i], porcentaje[i]]
        data.append(row)

    fig, ax = plt.subplots(figsize=(9, 8))
    ax.table(
        cellText=data,
        colLabels=['Estados', 'Población', '# Contagiados', 'Porcentaje'],
        loc="center"
    )
    ax.axis('tight')
    ax.axis('off')
    plt.title("Relacion de contagios en la población")


def show_bar(x, y):
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.bar(x, y)
    ax.set_ylabel("Porcentaje")
    plt.title("% Casos confirmados de acuerdo a la población")
    plt.xticks(x, rotation=90)
    plt.grid(True)

    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.25)


def graphics(estados, poblacion, contagios, porcentaje):
    show_tabla(estados, poblacion, contagios, porcentaje)
    show_bar(estados, porcentaje)
    plt.show()


def main():
    data = return_matriz()
    graphics(data[0], data[1], data[2], data[3])


if __name__ == "__main__":
    main()
