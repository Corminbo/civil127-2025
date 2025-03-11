import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()

    width, height = (800, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Game")

    radius = 50
    x = width / 2
    y = height / 2
    dx = 7
    dy = 9

    while True:
    # Limits the while loop to a max of 60 FPS
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
    # Fill the screen with a color (e.g., white)
        screen.fill((255, 255, 255))

    # Draw a circle going up and down
        pygame.draw.circle(screen, (128, 255, 128), [x,y], radius)
        pygame.display.flip()
        x += dx
        if x + radius >= width:
            x = width - radius
            dx = -dx
        elif x - radius <= 0:
            x = radius
            dx = -dx
            y += dy
        if y + radius >= height:
            y = height - radius
            dy = -dy
        elif y - radius <= 0:
            y = radius
            dy = -dy
main()