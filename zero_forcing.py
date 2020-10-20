"""
Simulate zero forcing on one graph.
"""


def simulate_zero_forcing(gr, initial_black_nodes):

    graph = gr.copy()
    nodes = graph.number_of_nodes()
    blacks = len(initial_black_nodes)
    last_blacks = 0
    steps = 0
    initial_blacks = blacks

    white_neighbors = []
    colors = []
    active_black_nodes = []

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

    while True:
        whites = nodes - blacks
        if (whites > 0) and (blacks > last_blacks):
            last_blacks = blacks
            steps += 1
            new_blacks, colors, active_black_nodes, white_neighbors = simulate_one_step(
                graph, colors, active_black_nodes, white_neighbors)
            blacks += new_blacks
        else:
            if blacks < nodes:
                print("Zero forcing failed")
                return initial_blacks, False
            else:
                print(f"Zero forcing finished in {steps} step(s)")
                return initial_blacks, True


def simulate_one_step(graph, colors, active_black_nodes, white_neighbors):

    new_blacks = 0

    for active_black in active_black_nodes.copy():
        if white_neighbors[active_black] == 1:
            for active_black_nb in graph.neighbors(active_black):
                if colors[active_black_nb] == 0:
                    colors[active_black_nb] = 1
                    new_blacks += 1
                    for active_black_nb_nb in graph.neighbors(active_black_nb):
                        white_neighbors[active_black_nb_nb] -= 1
                        if (white_neighbors[active_black_nb_nb] == 0) and (colors[active_black_nb_nb] == 1):
                            active_black_nodes.remove(active_black_nb_nb)
                    if white_neighbors[active_black_nb] > 0:
                        active_black_nodes.append(active_black_nb)
                    break

    return new_blacks, colors.copy(), active_black_nodes.copy(), white_neighbors.copy()
