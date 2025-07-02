import pygame
import sys

# Pygame initialisieren
pygame.init()

# Fenstergröße
width, height = 800, 600

# Fenster erstellen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mein erstes Pygame-Programm")

# Farben
white = (255, 255, 255)
blue = (0, 0, 255)

# Haupt-Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hintergrund weiß füllen
    screen.fill(white)

    # Blauen Kreis zeichnen
    pygame.draw.circle(screen, blue, (width // 2, height // 2), 50)

    # Anzeige aktualisieren
    pygame.display.flip()

# Beenden
pygame.quit()
sys.exit()
