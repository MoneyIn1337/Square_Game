import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Squares Game")

# Set the dimensions of the squares
square_size = 50

# Set the starting position of the squares
square_1_position = [100, 100]
square_2_position = [250, 250]

# Set the movement speed of the squares (in pixels per frame)
square_speed = 5

# Set the colors of the squares
square_1_color = (255, 0, 0) # red
square_2_color = (0, 255, 0) # green

# Set the game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move square 1
    if keys[pygame.K_w]:
        square_1_position[1] -= square_speed
    if keys[pygame.K_s]:
        square_1_position[1] += square_speed
    if keys[pygame.K_a]:
        square_1_position[0] -= square_speed
    if keys[pygame.K_d]:
        square_1_position[0] += square_speed

    # Move square 2
    if keys[pygame.K_UP]:
        square_2_position[1] -= square_speed
    if keys[pygame.K_DOWN]:
        square_2_position[1] += square_speed
    if keys[pygame.K_LEFT]:
        square_2_position[0] -= square_speed
    if keys[pygame.K_RIGHT]:
        square_2_position[0] += square_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the squares
    pygame.draw.rect(screen, square_1_color, pygame.Rect(square_1_position[0], square_1_position[1], square_size, square_size))
    pygame.draw.rect(screen, square_2_color, pygame.Rect(square_2_position[0], square_2_position[1], square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)