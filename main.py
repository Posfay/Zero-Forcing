import os
import sys
import zero_forcing_process as zf
import graph_utils


nodes = int(sys.argv[1])
n = 0

while True:
    n += 1

    graph, initial_black_nodes_list = zf.generate_initial_coloring(nodes)
    zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph, initial_black_nodes_list)
    graph_utils.write_graph_to_file(graph, zf_number, init_black_nodes_successful)

    if nodes <= 14:
        if n % 10 == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(n)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(n)
