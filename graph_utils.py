import time
import matplotlib.pyplot as plt
import networkx as nx


def generate_3_regular_graph(n, seed):

    graph = nx.random_regular_graph(3, n, seed)
    for i in list(graph.nodes):
        graph.nodes[i]['b'] = 0

    return graph


def draw_nx_graph(graph):

    options = {
        'node_color': 'black',
        'node_size': 100,
        'width': 3,
    }
    plt.subplot(121)
    nx.draw(graph, with_labels=True, font_weight='bold')
    # nx.draw_random(G, **options)
    plt.show()
