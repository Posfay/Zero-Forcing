import time
import zero_forcing
import subset_generating
import graph_utils

"""
Generate graphs and simulate zero forcing on them.
"""


def generate_graphs(n, seed=int(time.time())):
    """
    Generate 1 graph with all possible initial black nodes set.

    :param n: int
    :param seed: int
    :return: Graph
    """
    graphs = list()
    initial_black_nodes_list = list()

    # generate list of initial black nodes
    for i in range(2, int(n / 2) + 2):
        subset_generating.process_subsets(list(range(0, n)), i)
        subs = list(subset_generating.subsets)
        initial_black_nodes_list.extend(subs)

    # generate the core graph
    core_graph = graph_utils.generate_3_regular_graph(n, seed)
    # create the list of graphs
    for lst in initial_black_nodes_list:
        graph = core_graph.copy()
        for node in lst:
            graph.nodes[node]['b'] = 1
        graphs.append(graph)

    return graphs


def simulate_zero_forcing_on_graphs(graphs):
    """
    Simulate zero forcing on permutations of a graph and return Z(graph).

    :param graphs: list(Graph)
    :return: int
    """
    found_zero_forcing_number = False
    zero_forcing_number = 0
    nodes = graphs[0].number_of_nodes()

    print("Graph structure: {list(graphs[0].adjacency())}")

    for graph in graphs:
        g = graph.copy()
        initial_blacks, success = zero_forcing.simulate_zero_forcing(graph)
        print("{success} - {initial_blacks} - {g.nodes.data()}")

        if success and not found_zero_forcing_number:
            found_zero_forcing_number = True
            zero_forcing_number = initial_blacks

    print("The zero forcing number of the graph with {nodes} nodes is "
          "{zero_forcing_number}")

    return zero_forcing_number
