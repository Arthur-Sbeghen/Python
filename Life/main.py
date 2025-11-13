import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#use valores maiores que 170
VIVO = 300
MORTO = 0
valores = [VIVO, MORTO]

def grade_aleatoria(tamanho: int):
    """Cria uma grade aleatória com células vivas e mortas."""
    return np.random.choice(valores, tamanho * tamanho, p=[0.2, 0.8]).reshape(tamanho, tamanho)


def adicionar_planador(x: int, y: int, grade: np.ndarray):
    """Adiciona um planador (glider) à grade, começando na posição (x, y)."""
    planador = np.array([
        [0,    0, 255],
        [255,  0, 255],
        [0,  255, 255]
    ])
    grade[x:x+3, y:y+3] = planador


def adicionar_gun_gosper(x: int, y: int, grade: np.ndarray):
    """Adiciona o canhão de planadores de Gosper à grade."""
    gun = np.zeros(11 * 38).reshape(11, 38)

    # Cabeça do canhão
    gun[5][1] = gun[5][2] = 255
    gun[6][1] = gun[6][2] = 255

    # Corpo central
    gun[3][13] = gun[3][14] = 255
    gun[4][12] = gun[4][16] = 255
    gun[5][11] = gun[5][17] = 255
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
    gun[7][11] = gun[7][17] = 255
    gun[8][12] = gun[8][16] = 255
    gun[9][13] = gun[9][14] = 255

    # Extensão direita
    gun[1][25] = 255
    gun[2][23] = gun[2][25] = 255
    gun[3][21] = gun[3][22] = 255
    gun[4][21] = gun[4][22] = 255
    gun[5][21] = gun[5][22] = 255
    gun[6][23] = gun[6][25] = 255
    gun[7][25] = 255

    # Cauda final
    gun[3][35] = gun[3][36] = 255
    gun[4][35] = gun[4][36] = 255

    grade[x:x+11, y:y+38] = gun

def atualizar(frame_num, imagem, grade, tamanho):
    """Calcula a próxima geração do Jogo da Vida."""
    nova_grade = grade.copy()

    for i in range(tamanho):
        for j in range(tamanho):
            # Soma dos vizinhos vivos
            total = int((
                grade[i, (j-1) % tamanho] + grade[i, (j+1) % tamanho] +
                grade[(i-1) % tamanho, j] + grade[(i+1) % tamanho, j] +
                grade[(i-1) % tamanho, (j-1) % tamanho] + grade[(i-1) % tamanho, (j+1) % tamanho] +
                grade[(i+1) % tamanho, (j-1) % tamanho] + grade[(i+1) % tamanho, (j+1) % tamanho]
            ) / 255)

            # Regras do jogo
            if grade[i, j] == VIVO:
                if total < 2 or total > 3:
                    nova_grade[i, j] = MORTO
            else:
                if total == 3:
                    nova_grade[i, j] = VIVO

    imagem.set_data(nova_grade)
    grade[:] = nova_grade[:]
    return imagem,

def main():
    parser = argparse.ArgumentParser(description="Executa a simulação do Jogo da Vida de Conway.")

    parser.add_argument('--tamanho-grade', dest='tamanho', required=False)
    parser.add_argument('--arquivo-video', dest='arquivo', required=False)
    parser.add_argument('--intervalo', dest='intervalo', required=False)
    parser.add_argument('--planador', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    # Tamanho padrão da grade
    tamanho = 100
    if args.tamanho and int(args.tamanho) > 8:
        tamanho = int(args.tamanho)

    # Intervalo entre frames (em ms)
    intervalo_atualizacao = 20
    if args.intervalo:
        intervalo_atualizacao = int(args.intervalo)

    # Configuração inicial da grade
    if args.planador:
        grade = np.zeros(tamanho * tamanho).reshape(tamanho, tamanho)
        adicionar_planador(1, 1, grade)
    elif args.gosper:
        grade = np.zeros(tamanho * tamanho).reshape(tamanho, tamanho)
        adicionar_gun_gosper(10, 10, grade)
    else:
        grade = grade_aleatoria(tamanho)

    # Criação da figura e animação
    fig, ax = plt.subplots()
    imagem = ax.imshow(grade, interpolation='nearest', cmap='gray')
    animacao = animation.FuncAnimation(
        fig, atualizar, fargs=(imagem, grade, tamanho),
        frames=None,
        interval=intervalo_atualizacao,
        cache_frame_data=False
    )

    # Salvamento opcional em vídeo
    if args.arquivo:
        animacao.save(args.arquivo, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()


if __name__ == '__main__':
    main()