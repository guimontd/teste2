import pygame
import math

# Inicializando o pygame
pygame.init()

BRANCO = (255, 255, 255)

LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Basquetebol 3000")

# Carregar sprites
sprite_bola = pygame.image.load("bola.png")
sprite_cesta = pygame.image.load("cesta.png")
fundo_imagem = pygame.image.load("fundo.png")

# Redimensionar sprites e fundo
sprite_bola = pygame.transform.scale(sprite_bola, (50, 50))
sprite_cesta = pygame.transform.scale(sprite_cesta, (200, 200))
fundo_imagem = pygame.transform.scale(fundo_imagem, (LARGURA_TELA, ALTURA_TELA))

# Centralizar a cesta
cesta_largura = 200
cesta_altura = 200
cesta_pos_x = (LARGURA_TELA - cesta_largura) // 2
cesta_pos_y = 100

# Definir a bola (la ele)
bola_raio = 15
bola_x = 390
bola_y = ALTURA_TELA - 50
bola_vel_x = 0
bola_vel_y = 0
gravidade = 0.5
forca_base = 10  #controlar a força da bola (la ele dnv)

# Pontuação
pontos = 0
fonte = pygame.font.SysFont("Arial", 30)

# Função para desenhar o fundo
def desenhar_fundo():
    tela.blit(fundo_imagem, (0, 0))

# Função para desenhar a bola (kkkk)
def desenhar_bola():
    tela.blit(sprite_bola, (bola_x - bola_raio, bola_y - bola_raio))

# Função para desenhar a cesta
def desenhar_cesta():
    tela.blit(sprite_cesta, (cesta_pos_x, cesta_pos_y))

# Função para desenhar o jogo
def desenhar_jogo():
    desenhar_fundo()
    desenhar_cesta()
    desenhar_bola()
    # Exibir a pontuação
    texto = fonte.render(f'Pontos: {pontos}', True, BRANCO)
    tela.blit(texto, (10, 10))
    pygame.display.flip()

# Função para verificar se a bola entrou (la ele mil vez)
def verificar_cesta():
    global pontos
    centro_cesta_x = cesta_pos_x + cesta_largura // 2
    centro_cesta_y = cesta_pos_y + cesta_altura // 2
    distancia_centro = math.hypot(bola_x - centro_cesta_x, bola_y - centro_cesta_y)

    if distancia_centro < 30:  # Raio ajustado para o tamanho do aro
        pontos += 1
        resetar_bola()

# Função para resetar a bola
def resetar_bola():
    global bola_x, bola_y, bola_vel_x, bola_vel_y
    bola_x = LARGURA_TELA // 2
    bola_y = ALTURA_TELA - 50
    bola_vel_x = 0
    bola_vel_y = 0

# Função principal do jogo
def main():
    global bola_x, bola_y, bola_vel_x, bola_vel_y

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Calcular a direção e força do lançamento com base na distância do clique
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - bola_x
                dy = mouse_y - bola_y
                distancia = math.hypot(dx, dy)

                if distancia > 0:
                    escala_forca = min(distancia / 100, 3)  # Limitar a força máxima
                    bola_vel_x = (dx / distancia) * forca_base * escala_forca
                    bola_vel_y = (dy / distancia) * forca_base * escala_forca

        # Atualizar a física da bola
        if bola_vel_x != 0 or bola_vel_y != 0:
            bola_x += bola_vel_x
            bola_y += bola_vel_y
            bola_vel_y += gravidade

        verificar_cesta()

        if bola_y > ALTURA_TELA:
            resetar_bola()

        desenhar_jogo()
        pygame.time.Clock().tick(60)

    pygame.quit()

# Rodar o jogo
if __name__ == "__main__":
    main()