def conversor(tipo_pesos,valor_dolar):

    pesos = input("¿Cuántos pesos {} tienes?: ".format(tipo_pesos))
    pesos = float(pesos)

    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares")

menu = """ 

Bienvenido al converso de monedas😀
1 - Pesos colombianos
2 - Pesos argentinod
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor("colombianos",65)
elif opcion == '2':
    conversor("argentinos",3875)
elif opcion == '3':
    conversor("mexicanos",19.99)
else:
    print ('Ingresa una opcion correcta')

