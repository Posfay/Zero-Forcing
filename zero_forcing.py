import networkx as nx
import matplotlib.pyplot as plt


def simulate_zero_forcing(gr):

    graph = gr.copy()
    nodes = graph.number_of_nodes()
    last_blacks = 0
    steps = 0

    while True:
        blacks = 0
        whites = 0
        for i in list(graph.nodes):                         # count black nodes
            if graph.nodes[i]['b'] == 1:
                blacks += 1
        whites = nodes - blacks
        if (blacks < nodes) and (blacks > last_blacks):     # if one step does not create new black nodes -> end
            last_blacks = blacks
            steps += 1
            graph = simulate_one_step(graph, whites, steps).copy()  # continue simulation
        else:
            if blacks < nodes:
                print("Zero forcing failed")
            else:
                print("Zero forcing finished in " + str(steps) + " step(s)")
            break


def simulate_one_step(graph, white_nodes, step):

    next_graph = graph.copy()
    processed_whites = 0

    for i in list(graph.nodes):                         # iterate over nodes in graph
        if processed_whites == white_nodes:             # if all white nodes are processed -> nothing to do -> break
            break
        if graph.nodes[i]['b'] == 0:                    # if node is white
            processed_whites += 1
            for j in graph.neighbors(i):                # iterate over its neighbors
                if graph.nodes[j]['b'] == 1:            # if node is black
                    whites = 0
                    for k in graph.neighbors(j):        # iterate over its neighbors
                        if graph.nodes[k]['b'] == 0:    # find and count all white neighbors
                            whites += 1
                            if whites > 1:
                                break
                    if whites == 1:                     # if only one white neighbor
                        next_graph.nodes[i]['b'] = 1    # original node becomes black
                        break

    print("Step " + str(step) + " - " + str(next_graph.nodes.data()))
    return next_graph


G = nx.Graph()

G.add_node(0, b=0)
G.add_node(1, b=0)
G.add_node(2, b=0)
G.add_node(3, b=1)

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)

simulate_zero_forcing(G)

# options = {
#     'node_color': 'black',
#     'node_size': 100,
#     'width': 3,
# }
#
# plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# # nx.draw_random(G, **options)
# plt.show()

