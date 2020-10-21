import sys
import zero_forcing_process as zf
import graph_utils


nodes = int(sys.argv[1])

while True:
    graph, initial_black_nodes_list = zf.generate_initial_coloring(nodes)
    zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph, initial_black_nodes_list)
    graph_utils.write_graph_to_file(graph, zf_number, init_black_nodes_successful)
