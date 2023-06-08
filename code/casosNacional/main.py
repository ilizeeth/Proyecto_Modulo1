from matplotlib import pyplot as plt
import os


def transforma_datos(estados, fecha, maximo):
    datos = []
    for i in range(len(estados)):
        renglon = [estados[i], fecha[i], maximo[i]]
        datos.append(renglon)
    return datos


def tabla(matriz, column_labels):

    fig, ax = plt.subplots(figsize=(6, 8))
    ax.table(cellText=matriz, colLabels=column_labels, loc='center')
    ax.axis('tight')
    ax.axis('off')
    plt.show()


def grafica(x, y):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y)
    plt.xticks(x, rotation=90)
    plt.subplots_adjust(bottom=0.4)
    plt.title("Máximos # contagios por Estado")
    ax.set_xlabel("Estados")
    ax.set_ylabel("Contagios")
    plt.show()


def maximo_estados(matriz):
    res = []
    estados = []
    for i in range(1, len(matriz)-1):
        fila = matriz[i]
        estados.append(fila[2])
        maximo = 0
        for j in range(3, len(fila)-1):
            cantidad = fila[j]
            res2 = int(cantidad)
            if res2 > maximo:
                maximo = res2
        res.append(maximo)

    return res, estados


def datos_tabla(matriz):
    res = []
    estados = []
    fecha = []
    for i in range(1, len(matriz)):
        fila = matriz[i]
        estados.append(fila[2])
        maximo = 0
        dato = 0
        for j in range(3, len(fila)):
            cantidad = fila[j]
            res2 = int(cantidad)
            if res2 > maximo:
                maximo = res2
                dato = matriz[0][j]

        fecha.append(dato)
        res.append(maximo)

    return res, fecha, estados

    return estados


def main():
    path = os.path.dirname(__file__)
    datos = []

    with open(path+'/../../code/BD.csv', 'r') as f:
        linea = True
        while linea:
            linea = f.readline()
            if len(linea) > 0:  # Limpieza de datos
                linea = linea[:-1]  # Se elimina el ultimo enter
                fila = linea.split(',')
                datos.append(fila)
        resultado, estados = maximo_estados(datos)
        resultado2, fecha2, estados2 = datos_tabla(datos)
        r = transforma_datos(estados2, fecha2, resultado2)
        titulos = ['Estado', 'Fecha', 'Máximo']

        tabla(r, titulos)
        grafica(estados, resultado)


# /Users/paolamedina/Desktop/Diplomado/Proyecto_Modulo1/code/BD.csv
if __name__ == "__main__":
    main()
