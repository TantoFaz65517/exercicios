import random
from random import sample
def geras_carte(mod):
    if mod == "rapido":
        carte = []
        for x in range(2):
            linha = []
            for x in range(3):
                if x == 0:
                    linha.append(random.randint(1, 10))
                elif x == 1:
                    linha.append(random.randint(11, 20))
                else:
                    linha.append(random.randint(21, 30))                
    elif mod == "demorado":
            carte = []
            for x in range(3):
                linha = []
                for x in range(3):
                    if x == 0:
                        linha.append(random.randint(1, 10))
                    elif x == 1:
                        linha.append(random.randint(11, 20))
                    else:
                        linha.append(random.randint(21, 30))   

#a = ("demorado")
#geras_carte(a)

def carte_ex(carte, play, sort):
    hvgvvg


def bingus():
    modo = str(input("Selecione o modo de jogo(rapido/demorado): "))
    while modo not in ["rapido", "demorado"]:
        modo = str(input("Modo invalido! Selecione o modo de jogo(rapido/demorado): "))
    play = []
    carte = []
    
    carte_n = 2 if modo == "rapido" else 4
    for x in range (carte_n):
        nome = input(f"Nome do jogador {x + 1}: ")
        play.append(nome)
        carte.append(geras_carte(modo))
    sort = []
    game_end = False
    cartelas_fechadas = set()
    while not game_end:
        dezena = random.randid(1, 40)
        while dezena in sort:
            dezena = random.randid(1, 40)
        sort.append(dezena)
        carte_ex(carte, play, sort)
        for y, carte in enumerate(cart)

bingus()
        
        
#while not jogo_terminado:
#    dezena = random.randint(1, 40)
#    while dezena in sorteados:
#        dezena = random.randint(1, 40)
#    sorteados.append(dezena)