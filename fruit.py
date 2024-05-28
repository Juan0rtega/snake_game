import random
import pygame

class Fruit:
    color : tuple
    rect: pygame.Rect
    screen_size : tuple[int]
    
    def __init__(self, color:tuple=(250, 105, 118), screen_size = (600,600)) -> None:
        self.color = color
        self.screen_size = screen_size
        
        pos = self._new_position()
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        
        
    def update(self, surf: pygame.Surface) -> None:
        pygame.draw.rect(surf, self.color, self.rect)
        
    def _new_position(self) -> tuple[int, int]:
        return (random.randint(0, int(self.screen_size[0]/10)) * 10, random.randint(0, int(self.screen_size[1]/10)) * 10)
    
    def change_position(self) -> None:
        self.rect = self.rect.move_to(topleft = self._new_position())
        
    def get_rect(self) -> pygame.Rect:
        return self.rect