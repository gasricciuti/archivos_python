# Archivos [Python]
# Ejercicios de práctica

# Autor: Gaston Ricciuti
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    with open('stock.csv') as csvfile:
        data = list(csv.DictReader(csvfile))

        stock_tornillos_1 = int(data[0]['tornillos'])
        stock_tornillos_2 = int(data[1]['tornillos'])
        stock_tornillos_3 = int(data[2]['tornillos'])
        stock_tornillos_4 = int(data[3]['tornillos'])
        stock_tornillos_5 = int(data[4]['tornillos'])
        stock_tornillos_6 = int(data[5]['tornillos'])
        

        sumatoria = []
        sumatoria.append(stock_tornillos_1)
        sumatoria.append(stock_tornillos_2)
        sumatoria.append(stock_tornillos_3)
        sumatoria.append(stock_tornillos_4)
        sumatoria.append(stock_tornillos_5)
        sumatoria.append(stock_tornillos_6)

        suma = 0

        for i in sumatoria:
            suma += i

        print('Total de Tornillos: ', suma)

    csvfile.close()       
    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    with open('propiedades.csv') as csvfile:
        archivo = list(csv.DictReader(csvfile))

        cantidad_2amb = 0
        cantidad_3amb = 0

        for i in archivo:
            if i['ambientes'] == '2':
                cantidad_2amb += 1
            elif i['ambientes'] == '3':
                cantidad_3amb += 1

    print('Cantidad de departamentos de 2 ambientes: ', cantidad_2amb)
    print('Cantidad de departamentos de 3 ambientes: ', cantidad_3amb)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()