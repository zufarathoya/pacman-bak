from Game import *
from GAPopInit import *
from Crossover import *
from Selection import *
from Mutation import *

input_delay = 10

# parameters
game_length = 60            # also as chromosome_length, gene_count
pop_count = 10              # population count for each generation
mating_pool_size = 10       # how many individuals are probable to crossover
mating_times = 5            # how many times crossover attempted. child_count = 2 * mating_times
mutation_probability = 0.05
tournament_entrant_count = 2      # how many entree in a tournament


# one loop
populations = create_init_population_bin(game_length, pop_count)

def pacman_ga(populations):
    pop_fitnesses = [random.random() for x in range(len(populations))]
    mating_pool = [populations[random.randint(0, len(populations) - 1)] for i in range(mating_pool_size)]

    children = []
    for i in range(mating_times):

        # Pilih parent pake tournament
        parent1 = mating_pool[random.randint(0, len(mating_pool) - 1)]
        parent2 = mating_pool[random.randint(0, len(mating_pool) - 1)]
        child1, child2 = crossover(parent1, parent2)
        children.append(child1)
        children.append(child2)

    for i in range(len(children)):
        children[i] = mutation(children[i], mutation_probability)

    populations += children

    pop_fitnesses = []
    for i in range(len(populations)):
        game = Game()
        inputs = chromosome_bin_iterator(populations[i])
        game.injectInput(inputs, input_delay)
        game.run()

        points = game.pacman.points
        time_left = 0 if game.pacman.lives == 0 else game_length - game.frameElapsed // input_delay
        fitness = calculate_fitness(points, time_left)
        pop_fitnesses.append(fitness)
        print(f'individual {i+1}: fitness = {fitness}')
    
    # sort dan pilih n terbaik
    new_populations = []
    for i in range(pop_count):
        entries = []
        for k in range(tournament_entrant_count):
            l = random.randint(0, len(populations) - 1)
            entries.append((populations[l], pop_fitnesses[l]))
        winner = tournament(entries)
        new_populations.append(winner)

    populations = new_populations
    # print(len(populations))

    return populations

for i in range(10):
    print(f'generation {i+1}')
    populations = pacman_ga(populations)
    print('')

# end loop
