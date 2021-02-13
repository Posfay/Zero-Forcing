import os
import ast
import networkx as nx
import tkinter as tk
from tkinter import filedialog
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


def simulate_zf(graphs, n, origin_graph1_path, origin_graph2_path):

    dir_path = f"{origin_graph1_path[:-4]} - {origin_graph2_path[:-4]}"
    path = f"c:\\Users\\bened\\Documents\\Zero Forcing\\Edge Split Results\\{n}\\{dir_path}"

    d = 0
    o = len(graphs)
    for graph in graphs:
        zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph)
        graph_utils.write_graph_to_file(graph, zf_number, init_black_nodes_successful, path)
        d += 1
        print(f"   {d}/{o}. done")


root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilenames()
print(f"Selected {len(files)} graphs")

c = 0
for file in files:
    graph_file = open(file, "r")
    filename = os.path.basename(graph_file.name)
    edges = ast.literal_eval(graph_file.readline())
    n = int(len(edges) * 2 / 3)

    created_graphs = edge_split(edges, edges.copy())
    print(f"   {len(created_graphs)} graphs created")
    simulate_zf(created_graphs, (2 * n) + 2, filename, filename)

    c += 1
    print(f"{c}/{len(files)} finished")
