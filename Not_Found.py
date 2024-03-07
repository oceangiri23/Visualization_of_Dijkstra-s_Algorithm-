import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
window_width = 600
window_height = 300
screen = pygame.display.set_mode((window_width, window_height))


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

def show_message_box(title, message):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)

        # Calculate position to center the error box
        box_width = 300
        box_height = 100
        box_x = (window_width - box_width) // 2
        box_y = (window_height - box_height) // 2

        # Draw error box
        pygame.draw.rect(screen, gray, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height), 2)

        # Draw title
        title_text = font.render(title, True, black)
        title_rect = title_text.get_rect(center=(window_width // 2, box_y + 30))
        screen.blit(title_text, title_rect)

        # Draw message
        message_text = font.render(message, True, black)
        message_rect = message_text.get_rect(center=(window_width // 2, box_y + 70))
        screen.blit(message_text, message_rect)

        pygame.display.flip()

