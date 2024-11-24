import math
import pygame

from Constants import *
from SpriteSheet import Spritesheet
from SpriteSheet import Spritesheet
from Node import NodeMap
from Player import Pacman

class AutoPlayer(Pacman):
    def __init__(self, screen: pygame.Surface, filename, spritesheet: Spritesheet, nodeMap: NodeMap) -> None:
        super().__init__(screen, filename, spritesheet, nodeMap)
        self.currentMove = 0
        self.createDict()
    
    def createDict(self):
        nodeList = self.map.nodeList
        self.dict = {}
        for node in nodeList:
        
            pathWeight = TILEHEIGHT
            if nodeList.index(node) not in self.dict:
                    self.dict[nodeList.index(node)] = []

            if node.up is not None:
                self.dict[nodeList.index(node)].append((nodeList.index(node.up),pathWeight))
            if node.right is not None:
                self.dict[nodeList.index(node)].append((nodeList.index(node.right),pathWeight))
            if node.down is not None:
                self.dict[nodeList.index(node)].append((nodeList.index(node.down),pathWeight))
            if node.left is not None:
                self.dict[nodeList.index(node)].append((nodeList.index(node.left),pathWeight))

    #creates a heuristic value for every node on the map
    def createHeuristic(self, goalNode):
        nodeList = self.map.nodeList
        self.heuristic = [0]*len(nodeList)
        for node in range(len(nodeList)):
            self.heuristic[node] = math.sqrt(abs(math.pow(nodeList[goalNode].x - nodeList[node].x,2) + math.pow(nodeList[goalNode].y - nodeList[node].y,2)))

    #special insert for AStar triple
    def insert(self, lst, value):
        if not lst:
            lst.append(value)
            return
        for i in range(len(lst)):
            if value[1] + value[2] <= lst[i][1] + lst[i][2]:
                lst.insert(i,value)
                return
        lst.append(value)

    #A* algorithm
    def findPath(self, startNode: int, destination: int):
        self.createHeuristic(destination)
        queue = []
        queue.append(([startNode],0,self.heuristic[startNode]))
        explored = []
        while queue:
            dataPair = queue[0]
            del queue[0]
            path = dataPair[0]
            current = path[-1]
            if current == destination:
                self.path = path
                return path, dataPair[1]
            explored.append(current)
            for node in self.dict[current]:
                check = node[0]
                if check not in explored:
                    newPath = list(dataPair[0])
                    newPath.append(node[0])
                    self.insert(queue,(((newPath), dataPair[1] + node[1],self.heuristic[node[0]])))

    def moveSet(self, path):
        direction = path[0]
        del path[0]
        match direction:
            case 0:
                if self.position.up is not None:
                    
                    return 0
            case 1:
                if self.position.right is not None:
                    
                    return 1
            case 2:
                if self.position.down is not None:
                    
                    return 2
            case 3: 
                if self.position.left is not None:
                     
                    return 3

    def checkNode(self, path):
        if self.location == self.position.vector:
            self.move = self.moveSet(path)
        
        match self.move:
            case -1:
                pass
            case 0:
                if self.closed == 0:
                    self.sprite = self.spritesheet.getLargeSprite(8*TILEWIDTH,0*TILEHEIGHT,0)
                elif self.closed == 1 or self.closed == 3:
                    self.sprite = self.spritesheet.getLargeSprite(6*TILEWIDTH,0,0)
                else:
                    self.sprite = self.spritesheet.getLargeSprite(6*TILEWIDTH,2*TILEHEIGHT,0)                
                
                
                if self.position.up != None:
                    if self.location != pygame.math.Vector2(self.position.up.position()):
                        self.location += SPEED*self.position.lerp(self.position.up).normalize()
                        
                    else:
                        self.position = self.position.up
                        
            case 1:
                if self.closed == 0:
                    self.sprite = self.spritesheet.getLargeSprite(8*TILEWIDTH,0*TILEHEIGHT,0)
                elif self.closed == 1 or self.closed == 3:
                    self.sprite = self.spritesheet.getLargeSprite(2*TILEWIDTH,0,0)
                else:
                    self.sprite = self.spritesheet.getLargeSprite(2*TILEWIDTH,2*TILEHEIGHT,0)
                
                if self.position.right != None:
                    
                    if self.location != pygame.math.Vector2(self.position.right.position()):
                        self.location += SPEED*self.position.lerp(self.position.right).normalize()
                        
                    else:    
                        self.position = self.position.right
                        
            case 2:
                if self.closed == 0:
                    self.sprite = self.spritesheet.getLargeSprite(8*TILEWIDTH,0*TILEHEIGHT,0)
                elif self.closed == 1 or self.closed == 3:
                    self.sprite = self.spritesheet.getLargeSprite(4*TILEWIDTH,0,0)
                else:
                    self.sprite = self.spritesheet.getLargeSprite(4*TILEWIDTH,2*TILEHEIGHT,0)
                
                if self.position.down != None:
                    if self.location != pygame.math.Vector2(self.position.down.position()):
                        self.location += SPEED*self.position.lerp(self.position.down).normalize()
                    else:    
                        self.position = self.position.down
            case 3:
                if self.closed == 0:
                    self.sprite = self.spritesheet.getLargeSprite(8*TILEWIDTH,0*TILEHEIGHT,0)
                elif self.closed == 1 or self.closed == 3:
                    self.sprite = self.spritesheet.getLargeSprite(0*TILEWIDTH,0,0)
                else:
                    self.sprite = self.spritesheet.getLargeSprite(0*TILEWIDTH,2*TILEHEIGHT,0)
                
                if self.position.left != None:
                    
                    if self.location != pygame.math.Vector2(self.position.left.position()):
                        self.location += SPEED*self.position.lerp(self.position.left).normalize()
                    else:    
                        self.position = self.position.left
                        
        self.display()