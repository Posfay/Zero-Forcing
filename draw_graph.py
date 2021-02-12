import ast
import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

graph_file = open(file_path, "r")
edge_list = ast.literal_eval(graph_file.readline())
black_nodes = ast.literal_eval(graph_file.readline())
zf_number = len(black_nodes)
nodes = int(len(edge_list) * 2/3)

graph = nx.Graph()
graph.add_edges_from(edge_list)
color_map = []
for i in graph:
    if i in black_nodes:
        color_map.append("red")
    else:
        color_map.append("grey")

nx.draw_shell(graph, node_color=color_map, with_labels=True)
plt.show()
