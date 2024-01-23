import random

#Codigo vida:
ps_jugador = 100
ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100
#Jugador
while ps_jugador>0 and ps_oponente>0:
    ataque_jugador = input("ataque: ")
    if ataque_jugador == 'malicioso':
        defensa_oponente = defensa_oponente - 10

        if defensa_oponente <= 0:
            defensa_oponente = 1
    elif ataque_jugador == 'placaje':
        ps_oponente -= 35 * (100/defensa_oponente)

    elif ataque_jugador == 'ascuas':
        ps_oponente -= 20
    else:
        print('Tus ataques son placaje, malicioso y ascuas' )     
        pass #Pass sirve para no hacer nada en caso de dicho condicional.
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente == 1: #latigo
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 2:
        ps_jugador -= 35 * (defensa_jugador/100) #placaje
    elif ataque_oponente == 3:
        ps_jugador -= 40 #pistola de agua.

#final
        
if ps_oponente <= 0 and ps_jugador <= 0:
    print("esto es un empate")
elif ps_oponente <= 0: 
    print('muy bien, has ganado!!!')
else:
    print('Lo lamento, perdiste esta batalla')   