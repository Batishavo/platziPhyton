
def run():
    LIMITE = 10e6

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print ( "2 elevado a {} es igual a: {}".format(contador, potencia_2))
        contador+=   1
        potencia_2 = 2**contador




if __name__ == '__main__':
    run()