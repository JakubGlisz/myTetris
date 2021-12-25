import var
import figures
import numpy
import random
import pygame

class TILE_MANAGER:
    def __init__(self):
        self.board = numpy.empty([var.width, var.height], dtype=object)
        self.board.fill(False)
        self.freeze = 0

        self.shape = figures.SSHAPE()

    def drawBoard(self, screen):

        self.shape.draw(screen)
        
        for x in range(self.board.size//self.board[0].size):
            for y in range(self.board[0].size):
                if self.board[x][y]:
                    pos_x = x * var.size_of_tile
                    pos_y = y * var.size_of_tile
                    rect = rect = pygame.Rect(pos_x, pos_y, var.size_of_tile, var.size_of_tile)
                    pygame.draw.rect(screen, self.board[x][y], rect)
    
    def fall(self):
        self.shape.fall()

    def checkCollision(self):
        for tile in self.shape.tiles:
            if tile.x > var.width-1 or tile.x < 0:
                return True
            elif tile.y >= var.height-1:
                return True
            elif self.board[tile.x][tile.y]:
                return True
        return False

    def haveFallen(self):
        # on y + 1 there is a tile
        # or encountered world edge
        for tile in self.shape.tiles:
            if tile.y + 1 >= var.height:
                self.freezeHandle()
                #self.lay()
                return 1
            if self.board[tile.x][tile.y + 1]:
                self.freezeHandle()
                #self.lay()
                return 1
        return 0
    
    def freezeHandle(self):
        if self.freeze == var.FREEZE:
            self.lay()
            self.freeze = 0
        else:
            self.freeze += 1
    
    # return 1 if row is full, otherwise return 0
    def checkRow(self, y):
        sum = 0
        for i in range(var.width):
            if self.board[i][y]:
                sum += 1
        if sum == var.width:
            return 1
        else:
            return 0
    
    def clearRow(self, y):
        for i in range(var.width):
            self.board[i][y] = 0
    
    # shift all rows above y down by one
    def fallRow(self, y):
        for j in range(y, 1, -1):
            for i in range(var.width):
                self.board[i][j] = self.board[i][j-1]

    def scoreHandling(self):
        #Y = []
        #for tile in self.shape.tiles:
        #    Y.append(tile.y)
        #Y = numpy.unique(Y)
        for tile in self.shape.tiles:
            if self.checkRow(tile.y):
                while self.checkRow(tile.y):
                    self.clearRow(tile.y)
                    self.fallRow(tile.y)

    def lay(self):
        for tile in self.shape.tiles:
            self.board[tile.x][tile.y] = tile.color
        self.scoreHandling()
        self.spawnShape()
    
    def spawnShape(self):
        rand = random.randint(0,6)
        if rand == 0:
            self.shape = figures.STICK()
        elif rand == 1:
            self.shape = figures.CUBE()
        elif rand == 2:
            self.shape = figures.TSHAPE()
        elif rand == 3:
            self.shape = figures.LSHAPE()
        elif rand == 4:
            self.shape = figures.JSHAPE()
        elif rand == 5:
            self.shape = figures.ZSHAPE()
        elif rand == 6:
            self.shape = figures.SSHAPE()

    def moveLeft(self):
        self.freeze = 0
        x_min = self.shape.tiles[0].x
        for tile in self.shape.tiles:
            if x_min > tile.x:
                x_min = tile.x
        if x_min > 0:
            for tile in self.shape.tiles: # Check if user is not trying to move into the wall
                    if self.board[tile.x - 1][tile.y]:
                        return

            for tile in self.shape.tiles:
                tile.x -= 1

    def moveRight(self):
        self.freeze = 0
        x_max = self.shape.tiles[0].x
        for tile in self.shape.tiles:
            if x_max < tile.x:
                x_max = tile.x
        if x_max < var.width-1:
            for tile in self.shape.tiles: # Check if user is not trying to move into the wall
                    if self.board[tile.x + 1][tile.y]:
                        return

            for tile in self.shape.tiles:
                tile.x += 1