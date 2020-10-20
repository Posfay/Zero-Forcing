import time
import matplotlib.pyplot as plt
import networkx as nx

"""
Utility functions for graph operations
"""


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
