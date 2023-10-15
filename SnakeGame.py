import pygame
import random

x = pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (50, 100, 200)

screen_width = 900
screen_height = 500

gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)


def welcome():
    exit_game = False

    while not exit_game:
        gameWindow.fill(white)
        text_screen("welcome to snake game", black, 260, 250)
        text_screen("Press space key to play...", blue, 250, 280)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()

        pygame.display.update()
        clock.tick(30)


# create game loop
def gameLoop():
    # create  game variable
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55

    snake_size = 20
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    score = 0

    food_x = random.randint(20, screen_width - 50)
    food_y = random.randint(20, screen_height - 50)

    fps = 30
    snk_list = []
    snk_length = 1

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            text_screen(
                "Game over ! press enter to continue",
                red,
                200,
                250,
            )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score = score + 10
                print("Score: ", score)

                food_x = random.randint(30, screen_width - 70)
                food_y = random.randint(30, screen_height - 70)
                snk_length = snk_length + 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            text_screen(
                "Score: " + str(score) + "  HighScore: " + str(highscore), red, 5, 5
            )
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if (
                snake_x < 0
                or snake_y < 0
                or snake_x > screen_width
                or snake_y > screen_height
            ):
                game_over = True
                print("Game over")

            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
