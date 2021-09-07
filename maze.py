# Created by Victor Honorato Pinheiro 05/09/2021
'''
A game in python than generate random maze everytime. 
FULL PERMISSION FOR PERSONAL OR COMERCIAL USE
The maze generator use the Randomized Prim's algorithm
Check (https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm)
'''
import pygame
import time
import random

## Defining constants

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (213,50,80)

#Dimensions, please chose multiple of 10
WIDTH=600
HEIGHT=400

class maze():
    #initial state of the game
    def __init__(self, width, height):
        pygame.init()
        self.dis=pygame.display.set_mode((width,height))
        pygame.display.update()
        pygame.display.set_caption("Maze game!")
        self.game_over = False
        self.width = width
        self.height = height

    #Start the game and give instructions when to finish
    def start(self):
        

        pygame.display.update()
        while not self.game_over:
            for event in pygame.event.get():
                # Quit when clicked the close button
                if event.type == pygame.QUIT:
                    self.game_over=True

                print(event)
        
        
        pygame.quit()
        quit()
    
    def generate_maze(self):
        #fill display with blue
        self.dis.fill(RED)

        # Get the starting point of the algoritm (step 2 on the list), multiple of 10
        self.starting_height = int(random.random()*self.height)
        self.starting_width = int(random.random()*self.width)

        #verifying that free spot start at the edge:
        if self.starting_height == 0:
            self.starting_height = 10
        if self.starting_height == self.height:
            self.starting_height = self.height - 10
        if self.starting_width == 0:
            self.starting_width = 10
        if self.starting_width == self.width:
            self.starting_width = self.width - 10
        
        #now this block is a path and the walls around it should be add to a wall list
        pygame.draw.rect(self.dis, WHITE, [self.starting_width, self.starting_height, 10, 10])
        self.walls = []
        self.walls.append([self.starting_width-10, self.starting_height])
        pygame.draw.rect(self.dis,  BLACK, [self.starting_width-10,self.starting_height , 10, 10])
        self.walls.append([self.starting_width, self.starting_height-10])
        pygame.draw.rect(self.dis,  BLACK, [self.starting_width,self.starting_height-10 , 10, 10])
        self.walls.append([self.starting_width, self.starting_height+10])
        pygame.draw.rect(self.dis,  BLACK, [self.starting_width,self.starting_height+10 , 10, 10])
        self.walls.append([self.starting_width+10, self.starting_height])
        pygame.draw.rect(self.dis,  BLACK, [self.starting_width+10,self.starting_height , 10, 10])
        
        #Step 3 algo, pick a random cell from the wall list while there is walls there.
        
        while self.walls:
            #pick random wall
            self.rand_wall = self.walls[int(random.random()*len(self.walls)-1)]
            
            #Check if its a left wall
            if self.rand_wall[1] != 0:
                if self.dis.get_at((self.rand_wall[0]-10,self.rand_wall[1])) == RED and self.dis.get_at((self.rand_wall[0]+10,self.rand_wall[1])) == WHITE :
                    #Get numbere of surrounding walls
                    s_cells = self.surrounding_cells(self.rand_wall)
                    if s_cells < 2:
                        #new path
                        pygame.draw.rect(self.dis,  WHITE, [self.rand_wall[0], self.rand_wall[1] , 10, 10])

                        #Mark the new walls
                        #Upper cell
                        if (self.rand_wall[1] !=0):
                            if self.dis.get_at((self.rand_wall[0],self.rand_wall[1]-10)) == WHITE:
                                 pygame.draw.rect(self.dis,  BLACK, [self.rand_wall[0], self.rand_wall[1]-10 , 10, 10])
                            if [self.rand_wall[0],self.rand_wall[1]-10] not in self.walls:
                                self.walls.append([self.rand_wall[0],self.rand_wall[1]-10])

                        #Bottom cell
                        if (self.rand_wall[1] !=self.height-1):
                            if self.dis.get_at((self.rand_wall[0],self.rand_wall[1]+10)) == WHITE:
                                 pygame.draw.rect(self.dis,  BLACK, [self.rand_wall[0], self.rand_wall[1]-10 , 10, 10])
                            if [self.rand_wall[0],self.rand_wall[1]+10] not in self.walls:
                                self.walls.append([self.rand_wall[0],self.rand_wall[1]+10])

                        #left cell
                        if (self.rand_wall[0] !=0):
                            if self.dis.get_at((self.rand_wall[0]-10,self.rand_wall[1])) == WHITE:
                                 pygame.draw.rect(self.dis,  BLACK, [self.rand_wall[0]-10, self.rand_wall[1] , 10, 10])
                            if [self.rand_wall[0]-10,self.rand_wall[1]] not in self.walls:
                                self.walls.append([self.rand_wall[0]-10,self.rand_wall[1]])

                    #Delete wall       
                    for wall in self.walls:
                        if wall[0] == self.rand_wall[0] and wall[1] == self.rand_wall[1]:
                            self.walls.remove(wall)
                            break
                

                          
            #Check if its an upper wall
            if self.rand_wall[0] != 0:
                if self.dis.get_at((self.rand_wall[0],self.rand_wall[1]-10)) == RED and self.dis.get_at((self.rand_wall[0],self.rand_wall[1]+10)) == WHITE :
                    s_cells = self.surrounding_cells(self.rand_wall)
                    if s_cells < 2:
            
            #Check if its an bottom wall
            if self.rand_wall[0] != self.height - 10:
                if self.dis.get_at((self.rand_wall[0],self.rand_wall[1]+10)) == RED and self.dis.get_at((self.rand_wall[0],self.rand_wall[1]-10)) == WHITE :
                    s_cells = self.surrounding_cells(self.rand_wall)
                    if s_cells < 2:

            #Check if its a right wall
            if self.rand_wall[1] != self.width:
                if self.dis.get_at((self.rand_wall[0]+10,self.rand_wall[1])) == RED and self.dis.get_at((self.rand_wall[0]-10,self.rand_wall[1])) == WHITE :
                    s_cells = self.surrounding_cells(self.rand_wall)
                    if s_cells < 2:
            

    def surrounding_cells(self, rand_walls):
        s_cells = 0
        if self.dis.get_at((rand_walls[0],rand_walls[1]-10)) == WHITE:
            s_cells += 1
        if self.dis.get_at((rand_walls[0],rand_walls[1]+10)) == WHITE:
            s_cells += 1
        if self.dis.get_at((rand_walls[0]-10,rand_walls[1]-10)) == WHITE:
            s_cells += 1
        if self.dis.get_at((rand_walls[0]+10,rand_walls[1]-10)) == WHITE:
            s_cells += 1
        
        return s_cells
    




        

game = maze(WIDTH, HEIGHT)
game.generate_maze()
game.start()
