from GAPopInit import *

chro = create_init_chromosome_bin(16)

iter = chromosome_bin_iterator(chro)
for _ in range(16):
    print(iter.next())