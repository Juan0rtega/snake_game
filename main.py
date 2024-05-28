
import pygame
from snake import Snake
from fruit import Fruit
import random


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('snake game')
        
        self.screen = pygame.display.set_mode ((300,300))
        self.snake = Snake(length= 3, screen_size=(300,300))
        self.clock = pygame.time.Clock()
        self.fruit_pos = [random.randint(0, 60) * 10, random.randint(0, 60) * 10]
        self.running = True
        self.fruit = Fruit(color=(250, 105, 118), screen_size=(300,300))
        self.snake_tick = 0
        self.move_delay = 20
    
    
    def run(self):        
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        
    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.snake.change_direction(pygame.key.get_pressed())

    def _update(self) -> None:
        self.snake_tick += 1
        if self.snake_tick >= self.move_delay:
            self.snake.move()
            self.snake_tick = 0
        
        #collisions
        if self.snake.get_head().colliderect(self.fruit.get_rect()):
            self.snake.add_chunk()
            self.fruit.change_position()
            self.move_delay -= 5
        
        for body_chunk in self.snake.get_body():
            if self.snake.get_head().colliderect(body_chunk):
                self.snake.set_color((160,35,22))

    def _draw(self) -> None:
        self.screen.fill((0,0,0)) 
        self.snake.update(self.screen)
        self.fruit.update(self.screen)


if __name__ == '__main__': Game().run()