import networkx as nx
import subset_generating
import zero_forcing
import graph_utils
import zero_forcing_process as zf


graph, initial_black_nodes_list = zf.generate_initial_coloring(6)
zf_number = zf.simulate_zero_forcing_on_graphs(graph, initial_black_nodes_list)
