def simulate_zero_forcing(gr):

    graph = gr.copy()
    nodes = graph.number_of_nodes()
    last_blacks = 0
    steps = 0
    blacks = 0

    for i in list(graph.nodes):                                         # count initial black nodes
        if graph.nodes[i]['b'] == 1:
            blacks += 1
    initial_blacks = blacks

    while True:
        whites = nodes - blacks
        if (whites > 0) and (blacks > last_blacks):                     # if one step does not create new blacks -> end
            last_blacks = blacks
            steps += 1
            g, new_blacks = simulate_one_step(graph, whites, steps)     # continue simulation
            graph = g.copy()
            blacks += new_blacks
        else:
            if blacks < nodes:
                # print("Zero forcing failed")
                return initial_blacks, False
            else:
                # print("Zero forcing finished in " + str(steps) + " step(s)")
                return initial_blacks, True


def simulate_one_step(graph, white_nodes, step):

    next_graph = graph.copy()
    processed_whites = 0
    new_blacks = 0

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
                        new_blacks += 1                 # count the new black nodes
                        break

    # print("Step " + str(step) + " - " + str(next_graph.nodes.data()))

    return next_graph, new_blacks
