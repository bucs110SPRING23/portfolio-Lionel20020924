# it doesn'y work i still need some time to finish the code . I will try to regrade this lab soon 
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (800, 600)

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Set the caption of the screen
pygame.display.set_caption("Dart Game")

# Set the background color
background_color = (255, 255, 255)

# Set the dartboard colors
dartboard_color = (0, 0, 0)
inner_circle_color = (255, 0, 0)
outer_circle_color = (0, 255, 0)
line_color = (0, 0, 255)

# Set the position and size of the dartboard
dartboard_position = (0, 0)
dartboard_radius = 250

# Set the position and size of the inner circle
inner_circle_position = (0, 0)
inner_circle_radius = 50

# Set the position and size of the outer circle
outer_circle_position = (0, 0)
outer_circle_radius = 125

# Set the position and size of the line
line_position = (0, 0)
line_length = 500
line_width = 5

# Fill the background with the background color
screen.fill(background_color)

# Draw the dartboard
pygame.draw.circle(screen, dartboard_color, dartboard_position, dartboard_radius)
pygame.draw.circle(screen, inner_circle_color, inner_circle_position, inner_circle_radius)
pygame.draw.circle(screen, outer_circle_color, outer_circle_position, outer_circle_radius, width=5)

# Draw the line
pygame.draw.line(screen, line_color, line_position, (line_position[0] + line_length, line_position[1]), line_width)


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_position = pygame.mouse.get_pos()

            # Draw the dart at the mouse position
            dart_position = mouse_position
            dart_radius = 10
            dart_color = (0, 0, 0)
            pygame.draw.circle(screen, dart_color, dart_position, dart_radius)

            # Update the display
            pygame.display.flip()

# Quit Pygame
pygame.quit()
