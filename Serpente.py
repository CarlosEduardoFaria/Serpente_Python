import pygame, random
from pygame.locals import *

# Funcoes de Apoio
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

#função que recebe as posições da Snake e da maça para testar a colisão
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Definicao dos botoes de movimento
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Metodo Init Cria a tela
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

#Representada por uma lista que se move para a DIREITA
snake = [(200, 200), (210, 200), (220,200)]

#Cria a superficie da Snake no tamanho 10,10
snake_skin = pygame.Surface((10,10))
snake_skin.fill((153,204,50)) #Verde

#Gera a posição da mação de forma randômica
apple_pos = on_grid_random()

#Gera a maça no tamanho 10,10 (1 pixel)
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #vermelha

#Atribui o valor de direção inicial para a Direita
my_direction = RIGHT

#Limita o FPS através da função .tick
clock = pygame.time.Clock()

#Criação do Score na tela
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

#Captura os eventos enquanto o laço While do Game Over for falso
game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        #Estrutura condicional que realiza os movimentos
        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    #Verifica se "comeu" a maça e adiciona 1 ao score
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random() #Cria uma nova posição para a a maça
        snake.append((0,0)) #Faz com que a Snake aumente tomando a posição anterior
        score = score + 1
        
    # checar colisao com as bordas
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    # Verificar colisao com o proprio corpo
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    #Faz a movimentação da Snake
    for i in range(len(snake) - 1, 0, -1): #A ultima posição da cauda ocupara a posição -1 (anterior)
        snake[i] = (snake[i-1][0], snake[i-1][1]) #cada posição da Snake ira receber uma nova tupla
        
    # Fazer os movimentos - valores de X e Y
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    #COMANDO PARA LIMPAR A TELA
    screen.fill((0,0,0))

    #Cria a "imagem" da maça na tela
    screen.blit(apple, apple_pos)
    
    #Desenha os Pixels na tela de 10 em 10
    for x in range(0, 600, 10): # Draw Desenha Linhas Horizontais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Draw desenha linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    #Cria a "imagem" da Snake na tela
    for pos in snake:
        screen.blit(snake_skin,pos)

    #ATUALIZA O DISPLAY    
    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 200)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)

    #A dinâmica de Jogos possui um laço infinito que captura os eventos
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()