import random


def generarar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F','G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f','g']
    simbolos = ['!','#','$','&']
    numeros =['0','1','2','3','4','5','6','7','8','9','10']

    caracteres = mayusculas + minusculas + numeros + simbolos 
    contrasena = []
    for i in range (15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generarar_contrasena()
    print("Tu nueva contraena es: {}".format(contrasena))


if __name__ == '__main__':
    run()