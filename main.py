
import pygame
from snake import Snake
import random

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('snake game')
        
        self.screen = pygame.display.set_mode ((600,600))
        self.snake = Snake(length= 8)
        self.clock = pygame.time.Clock()
        self.fruit_pos = [random.randint(0, 60) * 10, random.randint(0, 60) * 10]
    
    
    def run(self):
        running = True
        
        while running:
            self.screen.fill((0,0,0))
            self.snake.move()
            self.snake.update(self.screen)
            pygame.draw.rect(self.screen, (250, 105, 118), pygame.Rect(*self.fruit_pos, 10, 10))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    self.snake.change_direction(pygame.key.get_pressed())
                    if pygame.key.get_pressed()[pygame.K_0]:
                        self.snake.add_chunk()
                    
            pygame.display.flip()
            self.clock.tick(12)
        pygame.quit()

if __name__ == '__main__': Game().run()