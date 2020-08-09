import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0, b=0)
G.add_node(1, b=0)
G.add_node(2, b=0)
G.add_node(3, b=1)

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)

# print(G.nodes.data())
# print(list(G.neighbors(0)))
# print(G.nodes[0]['b'])
# G2 = G.copy()
# G2.nodes[0]['b'] = 0
# print(G.nodes[0]['b'])
# print(G2.nodes[0]['b'])


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


def simulate_zero_forcing(gr):
    graph = gr.copy()
    nodes = graph.number_of_nodes()
    last_blacks = 0
    steps = 0
    while True:
        blacks = 0
        for i in list(graph.nodes):
            if graph.nodes[i]['b'] == 1:
                blacks += 1
        if (blacks < nodes) and (blacks > last_blacks):   # if one step does not create new black nodes -> end
            last_blacks = blacks
            steps += 1
            graph = simulate_one_step(graph, steps).copy()
        else:
            if blacks < nodes:
                print("Zero forcing failed")
            else:
                print("Zero forcing finished in " + str(steps) + " step(s)")
            break


def simulate_one_step(graph, step):
    next_graph = graph.copy()
    for i in list(graph.nodes):
        if graph.nodes[i]['b'] == 0:
            for j in graph.neighbors(i):
                if graph.nodes[j]['b'] == 1:
                    whites = 0
                    for k in graph.neighbors(j):
                        if graph.nodes[k]['b'] == 0:
                            whites += 1
                            if whites > 1:
                                break
                    if whites == 1:
                        next_graph.nodes[i]['b'] = 1
                        break
    print("Step " + str(step) + " - " + str(next_graph.nodes.data()))
    return next_graph


simulate_zero_forcing(G)
