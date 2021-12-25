import pygame
import var

class TILE:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.color = "#05d7f2"
    
    def draw(self, screen):
        pos_x = self.x * var.size_of_tile
        pos_y = self.y * var.size_of_tile
        rect = pygame.Rect(pos_x, pos_y, var.size_of_tile, var.size_of_tile)
        pygame.draw.rect(screen, self.color, rect)
    
    def fall(self):
        self.y += 1
    
    def transform(self, x, y):
        self.x += x
        self.y += y


class SHAPE:
    def rotateRight(self):
        for i, tiles in enumerate(self.tiles):
            tiles.transform(self.rotationVector[self.rot][i][0], self.rotationVector[self.rot][i][1])
        self.rot = (self.rot + 1) % len(self.rotationVector)
        
    def rotateLeft(self):
        index = (self.rot - 1) % len(self.rotationVector)
        for i, tiles in enumerate(self.tiles):
            tiles.transform(self.rotationVector[index][i][0]*-1, self.rotationVector[index][i][1]*-1)
        self.rot = index

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

    def fall(self):
          for tile in self.tiles:
              tile.fall()


class SSHAPE(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,1), TILE(5,1), TILE(5,0), TILE(6,0)]
        for tile in self.tiles:
            tile.color = "#e31724"
        self.rotationVector = [(1, -1), (0, 0), (-1,-1), (-2, 0)], \
                              [(-1, 1), (0, 0), (1,  1), (2, 0)]
        self.rot = 0

class ZSHAPE(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,0), TILE(5,0), TILE(5,1), TILE(6,1)]
        for tile in self.tiles:
            tile.color = "#323ee3"
        self.rotationVector = [(1, -1), (0, 0), (-1,-1), (-2, 0)], \
                              [(-1, 1), (0, 0), (1,  1), (2, 0)]
        self.rot = 0

class JSHAPE(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,0), TILE(5,0), TILE(6,0), TILE(6,1)]
        for tile in self.tiles:
            tile.color = "#ed3478"
        self.rotationVector = [(1, -1), (0, 0), (-1, 1), (-2, 0)], \
                              [(1,  1), (0, 0), (-1,-1), (0, -2)], \
                              [(-1, 1), (0, 0), (1, -1), (2,  0)], \
                              [(-1,-1), (0, 0), (1,  1), (0,  2)]
        self.rot = 0

class LSHAPE(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,1), TILE(4,0), TILE(5,0), TILE(6,0)]
        for tile in self.tiles:
            tile.color = "#eb9205"
        self.rotationVector = [(0, -2), (1, -1), (0, 0), (-1, 1)], \
                              [(2,  0), (1,  1), (0, 0), (-1,-1)], \
                              [(0,  2), (-1, 1), (0, 0), (1, -1)], \
                              [(-2, 0), (-1,-1), (0, 0), (1,  1)]
        self.rot = 0

class TSHAPE(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,0), TILE(5,0), TILE(6,0), TILE(5,1)]
        for tile in self.tiles:
            tile.color = "#9b05f2"
        self.rotationVector = [(1, -1), (0,0), (-1, 1), (-1,-1)], \
                              [(1,  1), (0,0), (-1,-1), (1, -1)], \
                              [(-1, 1), (0,0), (1, -1), (1,  1)], \
                              [(-1,-1), (0,0), (1,  1), (-1, 1)]
        self.rot = 0

class CUBE(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,0), TILE(5,0), TILE(4,1), TILE(5,1)]
        for tile in self.tiles:
            tile.color = "#cad10a"
        self.rotationVector = [(0,0), (0,0), (0,0), (0,0)], \
                              [(0,0), (0,0), (0,0), (0,0)]
        self.rot = 0

class STICK(SHAPE):
    def __init__(self):
        self.tiles = [TILE(4,0), TILE(5,0), TILE(6,0), TILE(7,0)]
        self.rotationVector = [(1,-1), (0,0), (-1,1), (-2,2)], \
                              [(-1,1), (0,0), (1,-1), (2,-2)]
        self.rot = 0
