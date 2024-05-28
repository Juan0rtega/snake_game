import pygame

CHUNK_SIZE = 10
X_AXIS = 'X'
Y_AXIS = 'Y'

class Snake:
    body_rects : list[pygame.Rect]
    current_mov_axis : str
    direction : int
    screen_size : tuple
    color : tuple
    
    def __init__(self, length: int = 3, start_pos: tuple[int] = (100,50), screen_size: tuple[int] = (600, 600)) -> None:
        self.current_mov_axis = X_AXIS
        self.screen_size = screen_size
        self.direction = 1
        self.body_rects = []
        self.color = (255,255,255)

        x_pos = start_pos[0]
        for _ in range(length):
            self.body_rects.append(pygame.Rect(x_pos, start_pos[1], CHUNK_SIZE, CHUNK_SIZE))
            x_pos -= 10

    def update(self, surf):
        for rect in self.body_rects:
            pygame.draw.rect(surf, self.color, rect)
        
            
    def move(self):
        offset = (self.direction * CHUNK_SIZE, 0) if self.current_mov_axis == X_AXIS else (0, self.direction * CHUNK_SIZE)
        new_rect = self.body_rects[0].move(*offset)

        for pos in range(len(self.body_rects)):
            copy_rect = self.body_rects[pos]
            self.body_rects[pos] = new_rect
            new_rect = copy_rect
            
    def change_direction(self, keys) -> None:
        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            return
        
        if self.current_mov_axis == X_AXIS:
            if keys[pygame.K_d]:
                self.direction = 1 if self.direction > 0 else -1
            if keys[pygame.K_a]:
                self.direction = -1 if self.direction  > 0 else 1

        if self.current_mov_axis == Y_AXIS:
            if keys[pygame.K_d]:
                self.direction = 1 if self.direction  < 0 else -1
            if keys[pygame.K_a]:
                self.direction = -1 if self.direction < 0 else 1
        
        self.current_mov_axis = Y_AXIS if self.current_mov_axis == X_AXIS else X_AXIS

    def add_chunk(self) -> None:
        self.body_rects.append(self.body_rects[-1].copy())
        
    def get_head(self) -> pygame.Rect:
        return self.body_rects[0]
    
    def get_body(self) -> list[pygame.Rect]:
        return self.body_rects[1:]
    
    def set_color(self, color) -> None:
        self.color = color