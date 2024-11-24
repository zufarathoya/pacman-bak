class SimulationParams:

    def __init__(self, game_length, pop_count, mating_times, mutation_probability, tournament_size, patience):
        self.game_length = game_length
        self.pop_count = pop_count
        self.mating_times = mating_times
        self.mutation_probability = mutation_probability
        self.tournament_size = tournament_size
        self.patience = patience

    def __repr__(self) -> str:
        return f'Params({self.game_length}, {self.pop_count}, {self.mating_times}, {self.mutation_probability}, {self.tournament_size}, {self.patience})'

params = SimulationParams(
    game_length = 60 * 60,
    pop_count = 3,
    mating_times = 2,
    mutation_probability = 0.1,
    tournament_size = 2,
    patience = 5
)

f = open("demofile3.txt", "w")
f.close()