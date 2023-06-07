import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos de la base de datos
data = pd.read_csv('datos.csv')  #'datos.csv' con los datos

def obtener_datos_lugar(nombre_lugar):
    while True:
        # Validar si el lugar existe en la base de datos
        if nombre_lugar == 'Nacional' or nombre_lugar in data['Lugar'].unique():
            datos_lugar = data[data['Lugar'] == nombre_lugar]
            break
        else:
            print("Lugar inválido.")
            nombre_lugar = input("Ingrese el nombre del lugar (puede ser el nombre del estado o 'Nacional'): ")

    # Obtener lista de meses
    datos_lugar['Fecha'] = pd.to_datetime(datos_lugar['Fecha'])
    datos_lugar['Mes'] = datos_lugar['Fecha'].dt.strftime('%m-%Y')
    
    # Calcular suma de casos confirmados por mes
    casos_por_mes = datos_lugar.groupby('Mes')['Casos Confirmados'].sum().tolist()
    
    # Graficar serie de datos
    plt.plot(datos_lugar['Mes'].unique(), casos_por_mes)
    plt.xlabel('Mes')
    plt.ylabel('Casos Confirmados')
    plt.title('Serie de datos por mes en ' + nombre_lugar)
    plt.show()

def main():
    print("Sistema de análisis de datos por lugar")
    nombre_lugar = input("Ingrese el nombre del lugar (puede ser el nombre del estado o 'Nacional'): ")
    obtener_datos_lugar(nombre_lugar)

if __name__ == '__main__':
    main()