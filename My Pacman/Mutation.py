import random
from GAPopInit import *


def mutation(child):
    n = len(child)
    li = [random.randint(0, 1 << 32 - 1) for i in range(n)]
    for i in range(n):
        child[i] ^= li[i]
    return child

def mutation(child, probability):
    n = len(child)
    li = [random.randint(0, 1 << 32 - 1) for i in range(n)]
    for i in range(n):
        if (random.random() < probability):
            child[i] = mutate_gene(child[i], probability)
    return child

def mutate_gene(gene, probability):
    for i in range(16):
        if (random.random() < probability):
            gene ^= random.randint(0, 3) << (i * 2)
    return gene