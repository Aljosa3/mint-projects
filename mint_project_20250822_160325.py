import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake class
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        current = self.get_head_position()
        x, y = self.direction
        new = ((current[0] + x) % GRID_WIDTH, (current[1] + y) % GRID_HEIGHT)
        
        if new in self.positions[3:]:
            return False
        
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
            
        return True

    def reset(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1

    def render(self, surface):
        for p in self.positions:
            rect = pygame.Rect(p[0] * GRID_SIZE, p[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

    def render(self, surface):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)

# Game class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        
        # Initialize display
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                    self.snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                    self.snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                    self.snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                    self.snake.direction = (1, 0)

    def run(self):
        while True:
            self.handle_keys()
            
            # Update snake
            if not self.snake.update():
                self.game_over()
                
            # Check if snake ate food
            if self.snake.get_head_position() == self.food.position:
                self.snake.length += 1
                self.score += 1
                self.food.randomize_position()
                
            # Draw
            self.display.fill(BLACK)
            self.snake.render(self.display)
            self.food.render(self.display)
            self.draw_score()
            pygame.display.update()
            
            self.clock.tick(10)  # Control game speed

    def game_over(self):
        self.display.fill(BLACK)
        game_over_text = self.font.render(f'Game Over! Score: {self.score}', True, WHITE)
        restart_text = self.font.render('Press SPACE to restart', True, WHITE)
        
        self.display.blit(game_over_text, 
                         (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                          WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
        self.display.blit(restart_text, 
                         (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                          WINDOW_HEIGHT//2 + restart_text.get_height()))
        
        pygame.display.update()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.snake.reset()
                        self.food.randomize_position()
                        self.score = 0
                        waiting = False

    def draw_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.display.blit(score_text, (10, 10))

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()