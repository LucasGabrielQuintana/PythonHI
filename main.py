
def main():
    tam = int(input('¿Que tamaño tiene su vector?\n'))
    print(tam)

    # ingreso_de_datos(tam)
    vector = ingreso_de_datos(tam)
    print(vector)


def ingreso_de_datos(dimension):
    vector = []
    for element in range(dimension):
        valor = int(input(f'Agregue un valor al elemento {element+1} => '))
        vector.append(valor)

    return vector



if __name__ == '__main__':
    main()