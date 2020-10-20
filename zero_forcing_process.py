import time
import networkx as nx
import zero_forcing
import subset_generating
import graph_utils

"""
Generate graphs and simulate zero forcing on them.
"""


def generate_initial_coloring(n, seed=int(time.time())):
    """
    Generate 1 graph with all permutations of initial black nodes.

    :param n: int
    :param seed: int
    :return: Graph
    """
    initial_black_nodes_list = list()

    # generate list of initial black nodes
    for i in range(2, int(n / 2) + 2):
        subs = subset_generating.process_subsets(list(range(0, n)), i)
        initial_black_nodes_list.extend(subs)

    # generate the core graph
    graph = nx.random_regular_graph(3, n, seed)

    return graph, initial_black_nodes_list


def simulate_zero_forcing_on_graphs(graph, initial_black_nodes_list):
    """
    Simulate zero forcing on permutations of a graph and return Z(graph).

    :param graph: list(Graph)
    :return: int
    """
    found_zero_forcing_number = False
    zero_forcing_number = 0
    nodes = graph.number_of_nodes()

    print(f"Graph structure: {list(graph.adjacency())}")

    for lst in initial_black_nodes_list:
        g = graph.copy()
        initial_blacks, success = zero_forcing.simulate_zero_forcing(graph, lst)
        print(f"{success} - {initial_blacks}")

        if success and not found_zero_forcing_number:
            found_zero_forcing_number = True
            zero_forcing_number = initial_blacks

    print(f"The zero forcing number of the graph with {nodes} nodes is " +
          f"{zero_forcing_number}")

    return zero_forcing_number
