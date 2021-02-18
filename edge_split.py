import datetime
import networkx as nx
import graph_utils
import zero_forcing_process as zf


def edge_split_one(edge_list1, edge_list2, e1, e2):
    """
    Creating a new graph with edge splitting.

    :param edge_list1: list(list(int))
    :param edge_list2: list(list(int))
    :param e1: list(int) (node1, node2)
    :param e2: list(int) (node1, node2)
    :return: Graph
    """
    n1 = int(len(edge_list1) * 2/3)
    n2 = int(len(edge_list2) * 2/3)
    edge_list1.remove(e1)
    edge_list2.remove(e2)
    new_edge_list2 = []
    for i in range(len(edge_list2)):
        new_edge_list2.append((edge_list2[i][0] + n1, edge_list2[i][1] + n1))
    nn1 = n1 + n2
    nn2 = n1 + n2 + 1
    ne = [(e1[0], nn1), (e1[1], nn1), (e2[0] + n1, nn2), (e2[1] + n1, nn2), (nn1, nn2)]

    new_graph = nx.Graph()
    new_graph.add_nodes_from(range(n1 + n2 + 2))
    new_edges = edge_list1 + new_edge_list2 + ne
    new_graph.add_edges_from(new_edges)

    return new_graph


def edge_split(edge_list1, edge_list2):
    """
    Creating every possible graphs from two graphs by edge splitting.

    :param edge_list1: list(list(int))
    :param edge_list2: list(list(int))
    :return: list(Graph)
    """
    new_graphs = []
    c = 0
    o = len(edge_list1) * len(edge_list2)
    for edge1 in edge_list1:
        for edge2 in edge_list2:
            new_graph = edge_split_one(edge_list1.copy(), edge_list2.copy(), edge1, edge2)
            c += 1
            isomorph = False
            for g in new_graphs:
                if nx.is_isomorphic(g, new_graph):
                    isomorph = True
                    break
            if not isomorph:
                new_graphs.append(new_graph)
                # print(f"{c}/{o}. added")
            else:
                pass
                # print(f"{c}/{o}. excluded")

    # print("finished edge splitting")
    return new_graphs


def simulate_zf(graphs, n, origin_graph1_path, origin_graph2_path, results_core_path):
    """
    Simulates zero forcing on the resulting graphs of edge splitting and saves the graphs

    :param graphs: list(Graph)
    :param n: int
    :param origin_graph1_path: str
    :param origin_graph2_path: str
    :param results_core_path:  str
    """
    dir_path = f"{origin_graph1_path[:-4]} - {origin_graph2_path[:-4]}"
    final_path = f"{results_core_path}\\{n}\\{dir_path}"

    d = 0
    o = len(graphs)
    for graph in graphs:
        t1 = datetime.datetime.now()
        zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph)
        graph_utils.write_graph_to_file(graph, zf_number, init_black_nodes_successful, final_path)

        d += 1
        t2 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()}    {d}/{o}."
              f" (n={n}, zf={zf_number}, ratio={round(zf_number/n, 2)})"
              f" done in {graph_utils.time_diff(t1, t2)}")
