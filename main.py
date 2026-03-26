from random import randint 

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

def jugar(usuario):
    
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

    reglas = {
        "piedra": ["tijera", "lagarto"],
        "papel": ["piedra", "spock"],
        "tijera": ["papel", "lagarto"],
        "lagarto": ["spock", "papel"],
        "spock": ["tijera", "piedra"]
    }
    
    indice_pc = randint(0, len(opciones) - 1)
    pc = opciones[indice_pc]

    print("-" * 30)
    print(f"Tú elegiste: {usuario.capitalize()}")
    print(f"La computadora eligió: {pc.capitalize()}")
    print("-" * 30)

    if usuario == pc:
        print("¡Es un empate!")
    elif pc in reglas[usuario]:
        print(f"¡GANASTE! {usuario.capitalize()} vence a {pc.capitalize()}.")
    else:
        print(f"PERDISTE. {pc.capitalize()} vence a {usuario.capitalize()}.")

print(
' _   _ _  _____ ____     _                      \n'+
'| | | | ||_   _|  _ \   / \                     \n'+
'| | | | |  | | | |_) | / _ \                    \n'+
'| |_| | |__| | |  _ < / ___ \                   \n'+
' \___/|____|_| |_| \_/_/   \_\                  \n'+
'                                                \n'+
'  ____    _    ____ _   _ ___ ____  _   _ _   _ \n'+
' / ___|  / \  / ___| | | |_ _|  _ \| | | | \ | |\n'+
'| |     / _ \| |   | |_| || || |_) | | | |  \| |\n'+
'| |___ / ___ \ |___|  _  || ||  __/| |_| | |\  |\n'+
' \____/_/   \_\____|_| |_|___|_|    \___/|_| \_|\n')

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