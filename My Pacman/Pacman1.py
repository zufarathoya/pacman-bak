from Game import *
from Simulation1 import *
from GAPopInit import *
from Crossover import *
from Mutation import *

# hyperparameters
max_generation = 250
patience = 5
basically_the_same_threshold = 0.001
game_length = 16       # also as chromosome_length, gene_count

input_delay = 10

def early_stop_check(n_last_fitnesses):
    c = len(n_last_fitnesses) - 1
    sum = 0
    for i in range(c):
        sum += abs(n_last_fitnesses[i+1] - n_last_fitnesses[i])
    return sum / c < basically_the_same_threshold

def tournament_selection(populations, pop_fitnesses, tournament_size):
    tournament = random.sample(
        list(zip(populations, pop_fitnesses)), tournament_size)
    # Pilih yang dengan fitness terbaik
    winner = max(tournament, key=lambda x: x[1])
    return winner[0]


def calculate_population_fitness(population):
    fitnesses = []
    i = 0
    for individual in population:
        game = Game()  # Inisialisasi game
        inputs = chromosome_bin_iterator(individual)
        game.injectInput(inputs, input_delay)
        game.run()

        points = game.pacman.points
        time_left = 0 if game.pacman.lives == 0 else game_length - \
            game.frameElapsed // input_delay
        fitness = calculate_fitness(points, time_left)

        print(f'Individual {i+1} Fitness: {fitness}')
        i += 1
        fitnesses.append(fitness)
    return fitnesses


def pacman_ga(populations, mating_times, mutation_probability, tournament_size):

    print(populations)

    pop_fitnesses = calculate_population_fitness(populations)

    mating_pool_size = len(populations)
    mating_pool = random.choices(
        populations, weights=pop_fitnesses, k=mating_pool_size)
    
    children = []
    for i in range(mating_times):
        parent1 = tournament_selection(
            mating_pool, pop_fitnesses, tournament_size)
        parent2 = tournament_selection(
            mating_pool, pop_fitnesses, tournament_size)

        child1, child2 = crossover(parent1, parent2)
        children.append(child1)
        children.append(child2)

    for i in range(len(children)):
        children[i] = mutation(children[i], mutation_probability)

    combined_population = populations + children
    children_fitnesses = calculate_population_fitness(children)

    combined_fitnesses = pop_fitnesses + children_fitnesses
    # combined_fitnesses = calculate_population_fitness(combined_population)

    sorted_individuals = sorted(
        zip(combined_population, combined_fitnesses), key=lambda x: x[1], reverse=True)

    average_fitness = sum(combined_fitnesses) / len(combined_fitnesses)
    max_fitness = sorted_individuals[0][1]

    print(f'generation max fitness {max_fitness}')
    print(f'generation avg fitness {average_fitness}')

    new_populations = [individual for individual,
                       fitness in sorted_individuals[:len(populations)]]

    return new_populations, (max_fitness, average_fitness)



# MAIN #


pop_count = 3               # population count for each generation
mating_times = 2            # how many times crossover attempted. child_count = 2 * mating_times
mutation_probability = 0.1  # probability of mutation
tournament_size = 3         # how many entree in a tournament

populations = create_init_population_bin(game_length, pop_count)

generation_history = []

for i in range(max_generation):
    print(f'generation {i+1}')
    populations, report = pacman_ga(populations, mating_times, mutation_probability, tournament_size)
    generation_history.append(report)

    # early stop if it's getting stagnant
    if (i >= patience) and early_stop_check(generation_history[-patience:]):
        break


    print('')

# end loop
