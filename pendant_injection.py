import networkx as nx


def inject_pendant_to_edge(graph, edge):
    """
    Creating a new graph by injecting a pendant to edge

    :param graph: Graph
    :param edge: list(int) (node1, node2)
    :return: Graph
    """
    orig_n = graph.number_of_nodes()

    # Creating pendant with a subdivided edge
    pendant_gr = nx.Graph(range(orig_n, orig_n + 4))
    pendant_gr.remove_edge(orig_n, orig_n + 1)
    new_pendant_edges = [(orig_n, orig_n + 4), (orig_n + 4, orig_n + 1)]
    original_pendant_edges = [e for e in pendant_gr.edges]
    pendant_edges = new_pendant_edges + original_pendant_edges

    # Injecting pendant to graph at edge
    original_graph_edges = [e for e in graph.edges]
    original_graph_edges.remove(edge)
    original_graph_edges = original_graph_edges + [(edge[0], orig_n + 5), (edge[1], orig_n + 5)]
    connecting_edge = [(orig_n + 4, orig_n + 5)]
    new_edges = original_graph_edges + pendant_edges + connecting_edge

    # Creating the nx graph
    new_graph = nx.Graph()
    new_graph.add_nodes_from(range(orig_n + 6))
    new_graph.add_edges_from(new_edges)

    return new_graph


def inject_pendants(graph):
    """
    Creating every new graph by injecting a pendant to every edge

    :param graph: Graph
    :return: list(Graph)
    """
    new_graphs = []
    edge_list = [e for e in graph.edges]
    c = 0
    o = len(edge_list)
    for edge in edge_list:
        new_graph = inject_pendant_to_edge(graph, edge)
        isomorph = False
        for g in new_graphs:
            if nx.is_isomorphic(g, new_graph):
                isomorph = True
                break
        if not isomorph:
            new_graphs.append(new_graph)
            c += 1

    print(f"Finished pendant injection, created {c}/{o} graphs")
    return new_graphs


def simulate_zf(graphs, core_path):
    pass
