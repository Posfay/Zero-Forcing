import time
import zero_forcing
import subset_generating
import graph_utils


def generate_graphs(n, seed=int(time.time())):                      # generate permutations of 1 graph with all
                                                                    # possible initial black nodes set
    graphs = list()
    initial_black_nodes_list = list()

    for i in range(2, int(n / 2) + 2):                              # generate list of initial black nodes
        subset_generating.process_subsets(list(range(0, n)), i)
        subs = list(subset_generating.subsets)
        initial_black_nodes_list.extend(subs)

    core_graph = graph_utils.generate_3_regular_graph(n, seed)      # generate the core graph
    for lst in initial_black_nodes_list:                            # create the list of graphs
        graph = core_graph.copy()
        for node in lst:
            graph.nodes[node]['b'] = 1
        graphs.append(graph)

    return graphs


def simulate_zero_forcing_on_graphs(graphs):                        # simulates zero forcing on a list of graphs

    found_zero_forcing_number = False
    zero_forcing_number = 0
    nodes = graphs[0].number_of_nodes()

    print("Graph structure: " + str(list(graphs[0].adjacency())))

    for graph in graphs:
        g = graph.copy()
        initial_blacks, success = zero_forcing.simulate_zero_forcing(graph)
        print(str(success) + " - " + str(initial_blacks) + " - " + str(g.nodes.data()))

        if success and not found_zero_forcing_number:
            found_zero_forcing_number = True
            zero_forcing_number = initial_blacks

    print("The zero forcing number of the graph with " + str(nodes) + " nodes is " + str(zero_forcing_number))
