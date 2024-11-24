import random

#int rep
def create_init_chromosome(chromosome_length):
    return [random.randint(0, 3) for _ in range(chromosome_length)]

def create_init_population(chromosome_length, pop_count):
    return [create_init_chromosome(chromosome_length) for _ in range(pop_count)]

class chromosome_iterator:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.i = 0

    def next(self):
        result = self.chromosome[self.i]
        i = (i + 1) % len(self.chromosome)
        return result
#int rep

#bin rep
int_bit_size = 32
gen_bit_size = 2
gen_per_int = int_bit_size // gen_bit_size
mask = 3

def create_init_chromosome_bin(chromosome_length):
    return [random.randint(0, 1 << int_bit_size - 1) for _ in range(chromosome_length // gen_per_int)]

def create_init_population_bin(chromosome_length, pop_count):
    return [create_init_chromosome_bin(chromosome_length) for _ in range(pop_count)]

class chromosome_bin_iterator:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.i = 0
        self.shift = 0

    def next(self):
        result = (self.chromosome[self.i] >> self.shift) & mask
        self.i = (self.i + 1) % len(self.chromosome)
        self.shift = (self.shift + gen_bit_size) % int_bit_size
        return result
#bin rep

def calculate_fitness(points, time_left):
    return 1 * points + 2 * time_left