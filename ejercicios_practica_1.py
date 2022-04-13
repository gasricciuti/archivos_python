# Archivos [Python]
# Ejercicios de práctica

# Autor: Gaston Ricciuti
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con diccionarios

import csv


def ej1():
    print('Ejercicios con diccionarios 1º')
    # Crear un diccionario vacio
    # el diccionario vacio debe llamarse "stock"
    
    # stock = ....

    # Luego de crear el diccionario completelo
    # con el siguiente stock:
    # tornillos = 100
    # tuercas = 150
    # arandelas = 300

    # Los nombres tornillos, tuercas y arandelas
    # son las claves (keys) del diccionario
    # mientras que las cantidades son los valores (values)

    # Una vez armado el diccionario imprimirlo en pantalla con print

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    stock = {}
    stock['tornillos'] = [100]
    stock['tuercas'] = [150]
    stock['arandelas'] = [300]

    print('El stock es:\n', stock)

def ej2():
    print('Ejercicio con diccionarios 2º')
    # Basado en el ejercicio anterior ej1, utilizaremos el diccionario
    # como una base de datos. Comenzaremos con un diccionario de stock
    # de nuestros productos en cero:
    
    stock = {'tornillos': 0, 'tuercas': 0, 'arandelas': 0}

    # Paso 1:
    # Crear un bucle utilizando while que se ejecute de forma infinita
    # while True.....
    
    # Paso 2:
    # Dentro de ese bucle consultar al usuario por consola
    # que producto desea agregar al stock
    #   - Si el usuario ingresa "FIN" como producto se debe 
    #   finalizar el bucle
    #   - Si el usuario ingresa un producto no definido en el stock
    #   se debe enviar un mensaje de error. (si desea investigar esto
    #   se resuelve muy bien utilizando el operador "in" con diccionarios)

    # Paso 3:
    # Luego de haber ingresado el producto se debe ingresar por consola
    # cuanto stock de ese producto se desea agregar al stock.
    # Si teniamos 20 tornillos y el usuario desea agregar 10 tornillos más,
    # en nuestro diccionario deben quedar 30 tornillos (debe acumular)

    # Paso 4:
    # Cuando el usuario ingrese "FIN" y se termine el bucle, debe
    # imprimir en pantalla con print el diccionario con el stock final

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    agregar = ''

    while True:
        print('''Ingrese que producto quiere agregar al stock:
a) tornillos
b) tuercas
c) arandelas
d) fin''')
        
        agregar = str(input('Ingresar el producto tal cual esta escrito: '))
        
        if agregar  == 'tornillos':
            print('Ingresar el stock de tornillos')
            try:
                stock['tornillos'] = int(input())
            except:
                print('Error al ingresar el stock')
        elif agregar == 'tuercas':
            print('Ingresar el stock tuercas')
            try:
                stock['tuercas'] = int(input())
            except:
                 print('Error al ingresar el stock')   
        elif agregar == 'arandelas':
            print('Ingresar el stock arandelas')
            try:
                stock['arandelas'] = int(input())
            except:
                print('Error al ingresar el stock')
        elif agregar == 'fin':
            print('Carga de stock finalizada')        
        else:
            print('Error al ingresar el stock')

        print('El stock final es:\n',stock)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()