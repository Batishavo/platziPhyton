def run():
    mi_dicionario={
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }
    # print (mi_dicionario['llave1'])
    # print (mi_dicionario['llave2'])
    # print (mi_dicionario['llave3'])
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil':210147125,
        'colombia': 50372424
    }
    #Keys
    #print(poblacion_paises['Bolivia'])
    # for pais in poblacion_paises.keys():
    #     print(pais)
    #Valor
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais, poblacion in poblacion_paises.items():
        print("{} tiene {} habitantes".format(pais, poblacion))


if __name__ == '__main__':
    run()