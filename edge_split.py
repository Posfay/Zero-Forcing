import ast
import datetime
import networkx as nx
import tkinter as tk
from tkinter import filedialog
import subset_generating
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
                print(f"{c}/{o}. added")
            else:
                print(f"{c}/{o}. excluded")

    print("finished edge splitting")
    return new_graphs


# Used for edge split creations
def write_es_graph_to_file(graph, zero_forcing_number, initial_black_nodes, path):

    nodes = graph.number_of_nodes()
    file_path = f"{path}\\{zero_forcing_number}_zf_{nodes}_nodes_"
    t = datetime.datetime.now()
    time_stamp = f"{t.strftime('%Y')}-{t.strftime('%m')}-" \
                 f"{t.strftime('%d')}_{t.strftime('%H')}-" \
                 f"{t.strftime('%M')}-{t.strftime('%S')}." \
                 f"{t.strftime('%f')}"
    extension = ".txt"
    final_file_path = file_path + time_stamp + extension

    file = open(final_file_path, "w")

    file.write(str(list(graph.edges)) + "\n")
    file.write(str(initial_black_nodes) + "\n")

    file.close()


def simulate_zf(graphs, n):

    path = "H:\\Data\\Zero Forcing\\Edge Split Results\\Test"
    initial_black_nodes_list = zf.generate_initial_coloring(n)

    c = 0
    o = len(graphs)
    for graph in graphs:
        zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph, initial_black_nodes_list)
        write_es_graph_to_file(graph, zf_number, init_black_nodes_successful, path)
        c += 1
        print(f"{c}/{o}. done")


root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilenames()
graph_file1 = open(files[0], "r")
edges1 = ast.literal_eval(graph_file1.readline())
nodes1 = int(len(edges1) * 2/3)
graph_file2 = open(files[1], "r")
edges2 = ast.literal_eval(graph_file2.readline())
nodes2 = int(len(edges2) * 2/3)

created_graphs = edge_split(edges1, edges2)
simulate_zf(created_graphs, nodes1 + nodes2 + 2)
