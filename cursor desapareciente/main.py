# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

fuente_simple = pygame.font.SysFont(None, 40)
texto_superficie = fuente_simple.render('preciona click para desaparecer el cursor', True, (255, 255, 255))
texto_rect = texto_superficie.get_rect(center=(640, 360))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Verifica si se presionó el botón izquierdo del mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("¡Botón izquierdo presionado!")
            pygame.mouse.set_visible(False)
            texto_superficie = fuente_simple.render('preciona click para desaparecer el cursor', True, (255, 255, 255))
        else:
            pygame.mouse.set_visible(True)
            texto_superficie = fuente_simple.render('deja de precionar el click para aparecer cursor', True, (255, 255, 255))


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    screen.blit(texto_superficie, texto_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()