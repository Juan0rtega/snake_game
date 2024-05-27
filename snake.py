import pygame

CHUNK_SIZE = 10
X_AXIS = 'X'
Y_AXIS = 'Y'

class Snake:
    body: list
    
    def __init__(self, length = 3, start_pos = (100,50), screen_size = (600, 600)) -> None:
        self.body = []
        self.current_mov_axis = X_AXIS
        self.screen_size = screen_size
        self.direction = 1
        x_pos = start_pos[0]
        
        for _ in range(length):
            self.body.append([x_pos, start_pos[1]])
            x_pos -= 10
        
    def update(self, surf):
        for pos in self.body:
            pygame.draw.rect(surf, (255,255,255), pygame.Rect(pos[0], pos[1], CHUNK_SIZE, CHUNK_SIZE))
            
    def move(self):
        if self.current_mov_axis == X_AXIS:
            new_value = [self.body[0][0] + (self.direction * CHUNK_SIZE), self.body[0][1]]
        if self.current_mov_axis == Y_AXIS:
            new_value = [self.body[0][0], self.body[0][1] + (self.direction * CHUNK_SIZE)]

            
        for i in range(len(self.body)):
            previous_value = self.body[i]
            
            if(new_value[0] > 600): new_value[0] = 0
            if(new_value[0] < 0): new_value[0] = 600
            
            if(new_value[1] > 600): new_value[1] = 0
            if(new_value[1] < 0): new_value[1] = 600
            
            self.body[i] = new_value
            new_value = previous_value
            
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
    
    def add_chunk(self):
        self.body.append([])