"""
Simulate zero forcing on one graph.
"""


def simulate_zero_forcing(gr, initial_black_nodes):
    """
    Find zero forcing number of a graph with some initially colored vertices.

    :param gr: Graph
    :param initial_black_nodes: list(int)
    :return: int, boolean
    """
    graph = gr.copy()
    nodes = graph.number_of_nodes()
    blacks = len(initial_black_nodes)
    last_blacks = 0
    steps = 0
    initial_blacks = blacks

    # Number of white neighbors a given node has
    white_neighbors = []
    # The color of a given node (0: white, 1: black)
    colors = []
    # List of active black nodes (those that have at least 1 white neighbor)
    active_black_nodes = []

    # initialisation of lists
    for i in range(nodes):
        colors.append(0)
        white_neighbors.append(graph.degree(i))

    for i in initial_black_nodes:
        colors[i] = 1
        for j in graph.neighbors(i):
            white_neighbors[j] -= 1

    for i in initial_black_nodes:
        if white_neighbors[i] > 0:
            active_black_nodes.append(i)

    # Simulation of the zero forcing process
    while True:
        whites = nodes - blacks
        # If there are still white nodes left, continue simulation
        if (whites > 0) and (blacks > last_blacks):
            last_blacks = blacks
            steps += 1
            # Simulate next iteration
            new_blacks, colors, active_black_nodes, white_neighbors = simulate_one_step(
                graph, colors, active_black_nodes, white_neighbors)
            blacks += new_blacks
        else:
            # If there are still white nodes after finish, zero forcing failed
            if blacks < nodes:
                print("Zero forcing failed")
                return initial_blacks, False
            else:
                print(f"Zero forcing finished in {steps} step(s)")
                return initial_blacks, True


def simulate_one_step(graph, colors, active_black_nodes, white_neighbors):
    """
    Simulate one iteration of zero forcing on a graph.

    :param graph: Graph
    :param colors: list(int)
    :param active_black_nodes: list(int)
    :param white_neighbors: list(int)
    :return: int, list(int), list(int), list(int)
    """
    new_blacks = 0

    # Iterate over active black nodes (copy to avoid skipping elements)
    for active_black in active_black_nodes.copy():
        # If a black node has only 1 white neighbor
        if white_neighbors[active_black] == 1:
            # Find the white among its neighbors
            for active_black_nb in graph.neighbors(active_black):
                if colors[active_black_nb] == 0:
                    # Color it black
                    colors[active_black_nb] = 1
                    new_blacks += 1
                    # Decrease number of white neighbors of the new black node
                    for active_black_nb_nb in graph.neighbors(active_black_nb):
                        white_neighbors[active_black_nb_nb] -= 1
                        # Remove any new inactive black nodes from the list
                        if ((white_neighbors[active_black_nb_nb] == 0)
                                and (colors[active_black_nb_nb] == 1)):
                            active_black_nodes.remove(active_black_nb_nb)
                    # If new black node is active, put it in the list
                    if white_neighbors[active_black_nb] > 0:
                        active_black_nodes.append(active_black_nb)
                    break

    return new_blacks, colors.copy(), active_black_nodes.copy(), white_neighbors.copy()
