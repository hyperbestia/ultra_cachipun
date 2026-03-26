from random import randint 

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

def jugar(usuario):
    pass




while True:
    try:
        print('Hola, juguemos al ultra cachipun, esta son las opciones:')
        for opcion in opciones:
            print(f'- {opcion}')
        
        opcion_usuario = input('Ingresa tu movimiento muajajaja: ')
        if opcion_usuario not in opciones:
            raise ValueError
        else:
            break
    except ValueError:
        print('Elige bien :v, coloca una opción de las que te coloqué')
jugar(opcion_usuario)