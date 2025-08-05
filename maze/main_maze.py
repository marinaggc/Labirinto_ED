# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque


# 1. Crie uma nova pilha. 
# A estrutura 'deque' é eficiente e pode ser usada como uma pilha.
stack = deque()

# --- Configuração Inicial do Labirinto ---
maze_csv_path = "labirinto1.txt"
maze = Maze()
maze.load_from_csv(maze_csv_path)

# Inicia a visualização gráfica do labirinto
maze.run()
# Posiciona o jogador (azul) e o prêmio (dourado) em locais aleatórios
maze.init_player()

# 2. Localize a posição inicial do jogador. 
start_pos = maze.get_init_pos_player()

# 3. Insira sua localização na pilha. 
stack.append(start_pos)

# Flag para indicar se o tesouro foi achado
path_found = False
print("Iniciando a busca pelo tesouro...")

# 4. Enquanto a pilha não estiver vazia... 
while stack:
    # 5. Retire uma localização da pilha. 
    current_pos = stack.pop()
    row, col = current_pos

    # 6. Mova o jogador para este local para visualização. 
    # A função 'mov_player' altera a cor do corredor, marcando-o como visitado.
    maze.mov_player(current_pos)

    # Adiciona uma pequena pausa para que a busca possa ser acompanhada visualmente.
    time.sleep(0.05)

    # 7. Se a posição atual contiver o prêmio... [cite: 13]
    if maze.find_prize(current_pos):
        # O caminho foi encontrado! [cite: 14]
        print("Tesouro encontrado!")
        path_found = True
        # Interrompe a busca. [cite: 15]
        break

    # 8. Caso contrário, examine as casas adjacentes. [cite: 16, 18]
    # A ordem de verificação (Sul, Leste, Norte, Oeste) afeta o caminho percorrido.
    neighbors = [
        (row + 1, col),  # Sul
        (row, col + 1),  # Leste
        (row - 1, col),  # Norte
        (row, col - 1)   # Oeste
    ]

    for next_pos in neighbors:
        # Se a casa adjacente for um corredor livre (não é parede nem foi visitada),
        # insira sua posição na pilha para explorá-la futuramente. 
        if maze.is_free(next_pos):
            stack.append(next_pos)

# Se a pilha esvaziar e o tesouro não for encontrado. 
if not path_found:
    print("Não foi possível encontrar um caminho para o tesouro.")

# Mantém a janela aberta para visualização do resultado final.
input("Busca finalizada. Pressione Enter para fechar o programa...")
