nombre1 = input("Como se llama el jugador 1? ")
nombre2 = input("Como se llama el jugador 2? ")

player1 = input("Hola Player 1! Elije entre Piedra, Papel o Tijeras: ")
player2 = input("Hola Player 2! Elije entre Piedra, Papel o Tijeras: ")

condicion1 = player1=="piedra" and player2=="tijeras"
condicion2 = player1=="papel" and player2=="piedra"
condicion3 = player1=="tijeras" and player2=="papel"

if player1 == player2:
    print("Ha sido un empate")
elif condicion1 or condicion2 or condicion3:
    print("Player 1 es el ganador!", nombre1)
else:
    print("El Player 2 es el ganador!", nombre2)


