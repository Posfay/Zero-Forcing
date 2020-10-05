import time
import matplotlib.pyplot as plt
import networkx as nx

"""
Utility functions for graph operations
"""


def generate_3_regular_graph(n, seed):
    """
    Generate a 3-regular graph with n vertices and return it.

    :param n: int
    :param seed: seed
    :return: Graph
    """
    graph = nx.random_regular_graph(3, n, seed)
    for i in list(graph.nodes):
        graph.nodes[i]['b'] = 0
        graph.nodes[i]['r'] = 0

    return graph


def draw_nx_graph(graph):
    """
    Visualise graph with matplotlib.

    :param graph: Graph
    """
    options = {
        'node_color': 'black',
        'node_size': 100,
        'width': 3,
    }
    plt.subplot(121)
    nx.draw(graph, with_labels=True, font_weight='bold')
    # nx.draw_random(G, **options)
    plt.show()
