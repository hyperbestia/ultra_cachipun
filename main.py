from random import randint 


    
opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

def jugar():
    
    print("--- Piedra, Papel, Tijera, Lagarto o Spock ---")
    
    opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
    
    print("\nSelecciona tu jugada:")
    for i in range(len(opciones)):
        print(f"{i + 1}. {opciones[i].capitalize()}")
    
    try:
        seleccion = int(input("\nIntroduce el número de tu opción: ")) - 1
        
        if seleccion < 0 or seleccion >= len(opciones):
            print("Opción fuera de rango. Inténtalo de nuevo.")
            return
            
        usuario = opciones[seleccion]
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
        return
    
    return usuario

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
jugar()