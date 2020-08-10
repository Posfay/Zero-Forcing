import time
import networkx as nx
import zero_forcing
import subset_generating
import graph_utils


def generate_graphs(n, seed=int(time.time())):

    graphs = list()
    initial_black_nodes_list = list()

    for i in range(2, int(n/2) + 2):     # n is even
        subset_generating.process_subsets(list(range(0, n)), i)
        subs = list(subset_generating.subsets)

        initial_black_nodes_list.extend(subs)

    core_graph = graph_utils.generate_3_regular_graph(n, seed)
    for lst in initial_black_nodes_list:
        graph = core_graph.copy()
        for node in lst:
            graph.nodes[node]['b'] = 1
        graphs.append(graph)

    return graphs


def simulate_zero_forcing_on_graphs(graphs):

    for graph in graphs:
        g = graph.copy()
        initial_blacks, success = zero_forcing.simulate_zero_forcing(graph)
        print(str(success) + " - " + str(initial_blacks) + " - " + str(g.nodes.data()) + " - " + str(list(g.adjacency())))
