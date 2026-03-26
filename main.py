opciones = ['PIEDRA', 'PAPEL', 'TIJERA', 'LAGARTO', 'SPOCK']

def jugar(eleccion):
    pass

while True:
    try:
        opcion_usuario = input('Ingresa tu movimiento muajajaja: ')
        if opcion_usuario not in opciones:
            raise ValueError
        else:
            break
    except ValueError:
        print('Elige bien :v, coloca una opción de las que te coloqué')
jugar()
    