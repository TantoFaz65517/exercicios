import random

def geras_carte(mod):
    carte = []
    if mod == "rapido":
        for x in range(2):
            linha = []
            for x in range(3):
                if x == 0:
                    linha.append(random.randint(1, 10))
                elif x == 1:
                    linha.append(random.randint(11, 20))
                else:
                    linha.append(random.randint(21, 30)) 
            carte.append(linha)
    elif mod == "demorado":
        for x in range(3):
            linha = []
            for x in range(3):
                if x == 0:
                    linha.append(random.randint(1, 10))
                elif x == 1:
                    linha.append(random.randint(11, 20))
                else:
                    linha.append(random.randint(21, 30))   
            carte.append(linha)

    return carte  # Retornar a cartela gerada

def carte_ex(carte, play, sort):
    for z, cartela in enumerate(carte):  # Mudando 'carte' para 'cartela'
        print(f"Cartela do jogador {play[z]}")
        for linha in cartela:  # Agora 'cartela' é a cartela do jogador
            linha_mark = []
            for num in linha:
                if num in sort:
                    linha_mark.append(f" ({num:2})")
                else:
                    linha_mark.append(f" {num:2}")
        print(" ".join(linha_mark))

def carte_state(carte, play, sort):
    print(f"Dezenas sorteadas: {' '.join(map(str, sorted(sort)))}")
    

def bingus():
    modo = str(input("Selecione o modo de jogo(rapido/demorado): "))
    while modo not in ["rapido", "demorado"]:
        modo = str(input("Modo invalido! Selecione o modo de jogo(rapido/demorado): "))
    play = []
    carte = []
    
    carte_n = 2 if modo == "rapido" else 4
    for x in range(carte_n):
        nome = input(f"Nome do jogador {x + 1}: ")
        play.append(nome)
        carte.append(geras_carte(modo))
    sort = []
    game_end = False
    cartelas_fechadas = set()
    while not game_end:
        dezena = random.randint(1, 40)
        while dezena in sort:
            dezena = random.randint(1, 40)
        sort.append(dezena)
        carte_ex(carte, play, sort)
        carte_state
        for y, cartela in enumerate(carte):
            if y in cartelas_fechadas:
                continue
            cartela_fechada = True
            for linha in cartela:
                for num in linha:
                    if num not in sort:
                        cartela_fechada = False
                        break
                if not cartela_fechada:
                    break
            if cartela_fechada:
                cartelas_fechadas.add(y)
                print(f"Jogador {play[y]} fechou a cartela!!")
        if len(cartelas_fechadas) == carte_n:
            game_end = True
        input("Precione a tecla Enter para sortear a próxima dezena")
    print("A partida acabou!")
    print("Vencedores:")
    for x in cartelas_fechadas:
        print(f"Jogador {play[x]}") 

bingus()
