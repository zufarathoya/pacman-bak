import random
from GAPopInit import *

def crossover(parent1, parent2):
    n = len(parent1)
    li = [random.randint(0, 1<<32-1) for i in range(n)]
    child1 = [0]*n
    child2 = [0]*n
    for i in range(n):
        child1[i] = (parent1[i] & ~li[i]) | (parent2[i] & li[i])
        child2[i] = (parent2[i] & ~li[i]) | (parent1[i] & li[i])
    return child1, child2
