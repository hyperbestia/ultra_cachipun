from random import randint 
#Modulo a ocupar

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