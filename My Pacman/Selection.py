def tournament(entries):
    max_entry = None
    max_fitness = 0 
    for entry, fitness in entries:
        if (fitness > max_fitness):
            max_fitness = fitness
            max_entry = entry
    return max_entry
