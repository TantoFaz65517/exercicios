import random
def gerar_cartela(modalidade):
    cartela = []
    if modalidade == "rápido":
        intervalos = [(1, 10), (11, 20), (21, 30)]
        for i in range(3):
            coluna = random.sample(range(intervalos[i][0], intervalos[i][1] + 1), 2)
            cartela.append(coluna)
    elif modalidade == "demorado":
        intervalos = [(1, 10), (11, 20), (21, 30), (31, 40)]
        for i in range(4):
            coluna = random.sample(range(intervalos[i][0], intervalos[i][1] + 1), 3)
            cartela.append(coluna)
    return cartela
def exibir_cartelas(cartelas, jogadores, sorteados):
    for i, cartela in enumerate(cartelas):
        print(f"\nCartela do jogador {jogadores[i]}:")
        for linha in cartela:
            linha_com_parenteses = []
            for num in linha:
                if num in sorteados:
                    linha_com_parenteses.append(f"({num:2})") 
                else:
                    linha_com_parenteses.append(f" {num:2} ") 
            print(' '.join(linha_com_parenteses))
        print()
def exibir_estado(sorteados, cartelas, jogadores):
    print(f"Dezenas sorteadas: {' '.join(map(str, sorted(sorteados)))}")
    exibir_cartelas(cartelas, jogadores, sorteados)
def bingus():
    modo = input("Escolha o modo de jogo (rapido/demorado): ").strip().lower()
    while modo not in ["rápido", "demorado"]:
        modo = input("Modo inválido! Escolha 'rapido' ou 'demorado': ").strip().lower()
    jogadores = []
    cartelas = []
    num_cartelas = 2 if modo == "rapido" else 4
    for i in range(num_cartelas):
        nome = input(f"Nome do jogador {i + 1}: ").strip()
        jogadores.append(nome)
        cartelas.append(gerar_cartela(modo))
    sorteados = []
    jogo_terminado = False
    cartelas_fechadas = set()
    while not jogo_terminado:
        dezena = random.randint(1, 40)
        while dezena in sorteados:
            dezena = random.randint(1, 40)
        sorteados.append(dezena)
        exibir_estado(sorteados, cartelas, jogadores)
        for i, cartela in enumerate(cartelas):
            if i in cartelas_fechadas:
                continue
            cartela_fechada = True
            for coluna in cartela:
                for num in coluna:
                    if num not in sorteados:
                        cartela_fechada = False
                        break
                if not cartela_fechada:
                    break
            if cartela_fechada:
                cartelas_fechadas.add(i)
                print(f"Jogador {jogadores[i]} fechou a cartela!")
        if len(cartelas_fechadas) == num_cartelas:
            jogo_terminado = True
        input("\nPressione Enter para sortear a próxima dezena...")
    print("\nFim do jogo!")
    print("Vencedores:")
    for i in cartelas_fechadas:
        print(f"Jogador {jogadores[i]}")

bingus()
print("shiu!!! ('0')")