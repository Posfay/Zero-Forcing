import networkx as nx
import zero_forcing
import subset_generating

"""
Generate graphs and simulate zero forcing on them.
"""


def generate_initial_coloring(n):
    """
    Generate all permutations of initial black nodes.

    :param n: int
    :return: list(list(int))
    """
    initial_black_nodes_list = list()

    # Generate list of initial black nodes
    for i in range(int(n / 3), int(n / 2) + 2):
        subs = subset_generating.process_subsets(list(range(0, n)), i)
        initial_black_nodes_list.extend(subs)

    return initial_black_nodes_list


def generate_graph(n):
    """
    Generating a connected 3 regular graph

    :param n: int
    :return: Graph
    """
    graph = nx.random_regular_graph(3, n)
    while True:
        # must be connected
        if nx.is_connected(graph):
            break
        graph = nx.random_regular_graph(3, n)

    return graph


def simulate_zero_forcing_on_graph(graph):
    """
    Find zero forcing number of graph.

    :param graph: Graph
    :return: int, list(int)
    """
    # Initialising the starting black node list for the next_subset generator
    nodes = graph.number_of_nodes()
    n = int(nodes / 3)
    subs = list(range(0, n))
    subs[n-1] -= 1
    t = 0

    # Simulate zero forcing on all *feasible* initial colorings
    while True:
        t += 1
        if t % 500000 == 0:
            print(f"{t} processed")

        subset_generating.next_subset(subs, nodes)
        # This should never be true
        if len(subs) >= int(nodes / 2) + 2:
            return -1, []

        zero_forcing_number, success = zero_forcing.simulate_zero_forcing(graph, subs)

        # First successful simulation gives Z(graph)
        if success:
            return zero_forcing_number, subs.copy()
