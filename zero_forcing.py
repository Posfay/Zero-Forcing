"""
Simulate zero forcing on one graph.
"""


def simulate_zero_forcing(gr):
    """
    Simulate zero forcing process on one graph and return Z(gr).

    :param gr: Graph
    :return: int, bool
    """
    graph = gr.copy()
    nodes = graph.number_of_nodes()
    last_blacks = 0
    steps = 0
    blacks = 0

    # count initial black nodes
    for i in list(graph.nodes):
        if graph.nodes[i]['b'] == 1:
            blacks += 1
    initial_blacks = blacks

    while True:
        whites = nodes - blacks
        # if one step does not create new blacks -> end
        if (whites > 0) and (blacks > last_blacks):
            last_blacks = blacks
            steps += 1
            # continue simulation
            g, new_blacks = simulate_one_step(graph, whites, steps)
            graph = g.copy()
            blacks += new_blacks
        else:
            if blacks < nodes:
                print("Zero forcing failed")
                return initial_blacks, False
            else:
                print(f"Zero forcing finished in {steps} step(s)")
                return initial_blacks, True


def simulate_one_step(graph, white_nodes, step):
    """
    Simulate one step of zero forcing on one graph and return modified graph.

    :param graph: Graph
    :param white_nodes: int
    :param step: int
    :return: Graph, int
    """
    next_graph = graph.copy()
    processed_whites = 0
    new_blacks = 0

    # iterate over nodes in graph
    for i in list(graph.nodes):
        # if all white nodes are processed -> nothing to do -> break
        if processed_whites == white_nodes:
            break
        # if node is white
        if graph.nodes[i]['b'] == 0:
            processed_whites += 1
            # iterate over its neighbors
            for j in graph.neighbors(i):
                # if node is black
                if graph.nodes[j]['b'] == 1:
                    whites = 0
                    # iterate over its neighbors
                    for k in graph.neighbors(j):
                        # find and count all white neighbors
                        if graph.nodes[k]['b'] == 0:
                            whites += 1
                            if whites > 1:
                                break
                    # if only one white neighbor
                    if whites == 1:
                        # original node becomes black
                        next_graph.nodes[i]['b'] = 1
                        # count the new black nodes
                        new_blacks += 1
                        break

    # print("Step " + str(step) + " - " + str(next_graph.nodes.data()))

    return next_graph, new_blacks
