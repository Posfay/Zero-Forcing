import os
import datetime
import networkx as nx
import graph_utils
import zero_forcing_process as zf


def inject_pendant_to_edge(edge_list, edge):
    """
    Creating a new graph by injecting a pendant to edge

    :param edge_list:list(list())
    :param edge: list(int) (node1, node2)
    :return: Graph
    """
    orig_n = int(len(edge_list) * 2 / 3)

    # Creating a pendant
    pendant_gr = nx.complete_graph(range(orig_n, orig_n + 4))
    pendant_gr.remove_edge(orig_n, orig_n + 1)
    new_pendant_edges = [(orig_n, orig_n + 4), (orig_n + 4, orig_n + 1)]
    original_pendant_edges = [e for e in pendant_gr.edges]
    pendant_edges = new_pendant_edges + original_pendant_edges

    # Injecting pendant to graph at edge
    original_graph_edges = edge_list.copy()
    original_graph_edges.remove(edge)
    original_graph_edges = original_graph_edges + [(edge[0], orig_n + 5), (edge[1], orig_n + 5)]
    connecting_edge = [(orig_n + 4, orig_n + 5)]
    new_edges = original_graph_edges + pendant_edges + connecting_edge

    # Creating the nx graph
    new_graph = nx.Graph()
    new_graph.add_nodes_from(range(orig_n + 6))
    new_graph.add_edges_from(new_edges)

    return new_graph


def inject_pendants(edge_list):
    """
    Creating every new graph by injecting a pendant to every edge

    :param edge_list: list(list(int))
    :return: list(Graph)
    """
    new_graphs = []
    c = 0
    o = len(edge_list)
    for edge in edge_list:
        new_graph = inject_pendant_to_edge(edge_list, edge)
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


def simulate_zf(graphs, n, zfn, origin_graph_path, results_core_path):
    """
    Simulates zero forcing on the resulting graphs of pendant injection and saves the graphs

    :param graphs: list(Graph)
    :param n: int
    :param zfn: int
    :param origin_graph_path: str
    :param results_core_path:  str
    """
    dir_path = f"{origin_graph_path[:-4]}"
    final_path = f"{results_core_path}\\{n}\\{dir_path}"

    d = 0
    o = len(graphs)
    max_zfn = 0
    orig_n = n - 6
    for graph in graphs:
        t1 = datetime.datetime.now()
        zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph)

        connecting_node = n - 1
        neighbors = [n for n in graph.neighbors(connecting_node)]
        neighbors.remove(max(neighbors))
        pendant_edge = tuple(neighbors)

        graph_utils.write_pendant_graph_to_file(graph, zf_number, init_black_nodes_successful, pendant_edge, final_path)

        if zf_number > max_zfn:
            max_zfn = zf_number

        orig_zf_ratio = zfn / orig_n
        current_zf_ratio = zf_number / n
        if current_zf_ratio >= orig_zf_ratio:
            save_stats(results_core_path, new_graphs_reached_ratio=1)

        save_stats(results_core_path, new_graphs_generated=1)

        d += 1
        t2 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()}    {d}/{o}."
              f" (n={n}, zf={zf_number}, ratio={round(zf_number / n, 2)})"
              f" done in {graph_utils.time_diff(t1, t2)}")

    orig_zf_ratio = zfn / orig_n
    max_zf_ratio = max_zfn / n
    if max_zf_ratio >= orig_zf_ratio:
        save_reached_ratio(results_core_path, origin_graph_path, orig_zf_ratio, max_zf_ratio)
        save_stats(results_core_path, original_graphs_reached_ratio=1)

    save_stats(results_core_path, original_graphs_processed=1)
    save_processed_graph(results_core_path, origin_graph_path)


def save_stats(results_core_path, original_graphs_processed=0,
               new_graphs_generated=0, original_graphs_reached_ratio=0, new_graphs_reached_ratio=0):
    """
    Saves statistics about the graph generation

    :param results_core_path: str
    :param original_graphs_processed: int - Number of graphs that were inputted for pendant injection
    :param new_graphs_generated: int - Number of graphs generated from pendant injection
    :param original_graphs_reached_ratio: int - Number of original graphs that produced at least one graph which
                                                reached the original one's zero forcing ratio
    :param new_graphs_reached_ratio: int - Number of new graphs that reached their respective original graph's zf ratio
    """
    stats_path = f"{results_core_path}\\stats.txt"

    if os.path.exists(stats_path):
        stats_file = open(stats_path, "r")
        original_graphs_processed += int(stats_file.readline())
        new_graphs_generated += int(stats_file.readline())
        original_graphs_reached_ratio += int(stats_file.readline())
        new_graphs_reached_ratio += int(stats_file.readline())
        stats_file.close()

    stats_file = open(stats_path, "w")
    stats_file.write(f"{str(original_graphs_processed)}\n")
    stats_file.write(f"{str(new_graphs_generated)}\n")
    stats_file.write(f"{str(original_graphs_reached_ratio)}\n")
    stats_file.write(f"{str(new_graphs_reached_ratio)}\n")
    stats_file.close()


def save_processed_graph(results_core_path, original_graph_name):
    """
    Saves original graphs that have already been processed

    :param results_core_path: str
    :param original_graph_name: str
    """
    processed_dir_path = f"{results_core_path}\\Processed Graphs"

    try:
        os.makedirs(processed_dir_path)
    except:
        pass

    processed_graph_path = f"{processed_dir_path}\\{original_graph_name}"
    processed_graph_file = open(processed_graph_path, "w")
    processed_graph_file.write(" ")
    processed_graph_file.close()


def save_reached_ratio(results_core_path, reached_graph_name, orig_zf_ratio, new_zf_ratio):
    """
    Saves graphs that reached their respective original graph's zf ratio

    :param results_core_path: str
    :param reached_graph_name: str
    :param orig_zf_ratio: float
    :param new_zf_ratio: float
    """
    reached_dir_path = f"{results_core_path}\\Graphs Reached Original Ratio"

    try:
        os.makedirs(reached_dir_path)
    except:
        pass

    new_graph_reached_path = f"{reached_dir_path}\\{reached_graph_name[:-4]} - " \
                             f"{str(round(new_zf_ratio, 3))}_new_{str(round(orig_zf_ratio, 3))}_orig.txt"
    new_graph_reached_file = open(new_graph_reached_path, "w")
    new_graph_reached_file.write(" ")
    new_graph_reached_file.close()
