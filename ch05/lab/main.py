import pygame
def threenp1(n):
    while n > 1.0:
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return None

def threenp1(start):
    count = 0
    n = start
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
    return count


def three_n_plus_1(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        count += 1
    return count

def count_iterations(lower_limit, upper_limit):
    objs_in_sequence = {}
    for i in range(lower_limit, upper_limit+1):
        for j in range(2, i+1):
            count = three_n_plus_1(j)
            if count not in objs_in_sequence:
                objs_in_sequence[count] = []
            objs_in_sequence[count].append(j)
    return objs_in_sequence


# B
import pygame

def threenp1(start):
    count = 0
    n = start
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
    return count

def threenp1range(lower, upper):
    results = {}
    for n in range(lower, upper+1):
        results[n] = threenp1(n)
    return results

def graph_coordinates(data_dict, width, height):
    max_iter = max(data_dict.values())
    points = []
    for n, iterations in data_dict.items():
        x = int(width * (n - 2) / (len(data_dict) - 2))
        y = int(height - height * (iterations / max_iter))
        points.append((x, y))
    return points

def main():
    pygame.init()

    # Set up screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('3n+1 Graph')

    # Set upper limit of range
    upper_limit = 100

    # Get coordinates for graph
    data_dict = threenp1range(2, upper_limit)
    coordinates = graph_coordinates(data_dict, screen_width, screen_height)

    # Draw graph
    screen.fill((255, 255, 255))
    if len(coordinates) > 1:
        pygame.draw.lines(screen, (255, 0, 0), False, coordinates, 2)

    # Show maximum iterations
    max_iterations = max(data_dict.values())
    message = f'Max iterations: {max_iterations}'
    font = pygame.font.Font(None, 30)
    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.flip()

    # Wait for user to close window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    main()

