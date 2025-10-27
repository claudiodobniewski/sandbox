import pygame
import random
import sys

# --- 1. Inicialización de Pygame ---
pygame.init()

# --- 2. Configuración de la Ventana y Colores ---
# Dimensiones de la ventana (simulando un "recuadro" pequeño como el alma de Undertale)
WIDTH = 600
HEIGHT = 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquivar cosas")

# Colores (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) # El color del jugador (el alma)
BLUE = (0, 0, 255) # Color de los obstáculos

# Fuente para el texto
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# --- 3. Variables del Juego ---
FPS = 60
clock = pygame.time.Clock()
game_over = True
score = 0

# --- 4. Configuración del Jugador (El Alma) ---
PLAYER_SIZE = 25
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 50  # Un poco arriba del fondo
player_speed = 7
player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)

# --- 5. Configuración de Obstáculos ---
obstacle_list = []
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 30
OBSTACLE_SPEED = 5
obstacle_spawn_rate = 60  # Cuantos frames deben pasar para generar un nuevo obstáculo
frames_since_last_spawn = 0

# --- 6. Funciones Auxiliares ---

def spawn_obstacle():
    """Genera un nuevo obstáculo con posición X aleatoria."""
    x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    y = -OBSTACLE_HEIGHT  # Empieza fuera de la pantalla por arriba
    obstacle_rect = pygame.Rect(x, y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    obstacle_list.append(obstacle_rect)

def update_obstacles(speed):
    """Mueve los obstáculos hacia abajo y elimina los que salieron de la pantalla."""
    global score
    for obstacle in obstacle_list[:]:
        obstacle.y += speed
        # Si el obstáculo pasa al jugador, aumenta el puntaje
        if obstacle.top > HEIGHT:
            obstacle_list.remove(obstacle)
            score += 1

def draw_objects():
    """Dibuja el jugador y todos los obstáculos en la pantalla."""
    # Dibujar jugador (Alma roja)
    pygame.draw.rect(SCREEN, RED, player_rect)
    # Dibujar obstáculos (Cuadrados azules)
    for obstacle in obstacle_list:
        pygame.draw.rect(SCREEN, BLUE, obstacle)

def check_collisions():
    """Verifica si el jugador colisionó con algún obstáculo."""
    for obstacle in obstacle_list:
        if player_rect.colliderect(obstacle):
            return True
    return False

def draw_score():
    """Muestra el puntaje actual en la esquina superior."""
    score_text = small_font.render(f"Puntaje: {score}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))

def draw_game_over():
    """Dibuja la pantalla de Game Over."""
    SCREEN.fill(BLACK)
    
    title = font.render("¡Has sido alcanzado!", True, RED)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    SCREEN.blit(title, title_rect)
    
    final_score = small_font.render(f"Puntaje Final: {score}", True, WHITE)
    score_rect = final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
    SCREEN.blit(final_score, score_rect)

    restart_msg = small_font.render("Presiona ESPACIO para Reintentar", True, WHITE)
    restart_rect = restart_msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    SCREEN.blit(restart_msg, restart_rect)

    pygame.display.flip()
    
def reset_game():
    """Reinicia todas las variables del juego."""
    global game_over, score, obstacle_list, player_rect
    game_over = False
    score = 0
    obstacle_list.clear()
    player_rect.center = (WIDTH // 2, HEIGHT - PLAYER_SIZE - 50)


# --- 7. Bucle Principal del Juego ---
while True:
    
    # 7.1 Manejo de Eventos (Teclado, Cierre de Ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Manejo del reinicio en Game Over
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_game()

    if game_over:
        
        # 7.2 Lógica del Movimiento del Jugador
        keys = pygame.key.get_pressed()
        
        # Mueve el jugador si las teclas están presionadas
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += player_speed
            
        # Asegurarse de que el jugador no salga de la pantalla
        player_x = max(0, min(player_x, WIDTH - PLAYER_SIZE))
        player_y = max(0, min(player_y, HEIGHT - PLAYER_SIZE))
        
        # Actualizar la posición del rectángulo del jugador
        player_rect.x = player_x
        player_rect.y = player_y

        # 7.3 Lógica de Obstáculos
        frames_since_last_spawn += 1
        if frames_since_last_spawn > obstacle_spawn_rate:
            spawn_obstacle()
            frames_since_last_spawn = 0
            
            # Aumentar la dificultad con el tiempo
            OBSTACLE_SPEED = 5 + (score // 15)  # Aumenta la velocidad cada 15 puntos
            
        update_obstacles(OBSTACLE_SPEED)

        # 7.4 Detección de Colisiones
        if check_collisions():
            game_over = True

        # 7.5 Dibujar todo
        SCREEN.fill(WHITE) # Fondo blanco
        draw_objects()
        draw_score()
        
    else:
        # Si el juego terminó, dibujar la pantalla de Game Over
        draw_game_over()

    # 7.6 Actualizar la pantalla (mostrar lo que se dibujó)
    pygame.display.flip()

    # 7.7 Controlar la velocidad del juego
    clock.tick(FPS)
