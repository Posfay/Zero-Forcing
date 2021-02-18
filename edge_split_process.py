import os
import ast
import datetime
import tkinter as tk
from tkinter import filedialog
import edge_split
import graph_utils


root = tk.Tk()
root.withdraw()


def edge_split_itself():

    results_dir_path = select_dir()
    files = select_files_itself()

    s1 = datetime.datetime.now()
    c = 0
    for file in files:
        s2 = datetime.datetime.now()
        graph_file = open(file, "r")
        filename = os.path.basename(graph_file.name)
        edges = ast.literal_eval(graph_file.readline())
        n = int(len(edges) * 2 / 3)

        s3 = datetime.datetime.now()
        created_graphs = edge_split.edge_split(edges, edges.copy())
        e3 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()}    {len(created_graphs)} graphs created in {graph_utils.time_diff(s3, e3)}")
        edge_split.simulate_zf(created_graphs, (2 * n) + 2, filename, filename, results_dir_path)

        c += 1
        e2 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()} {c}/{len(files)} finished in {graph_utils.time_diff(s2, e2)}")
    e1 = datetime.datetime.now()
    print()
    print(f"{graph_utils.timestamp()} Total run time: {graph_utils.time_diff(s1, e1)}")


def edge_split_other():

    results_dir_path = select_dir()
    file1, file2 = select_files_other()

    s1 = datetime.datetime.now()
    graph_file1 = open(file1, "r")
    graph_file2 = open(file2, "r")
    filename1 = os.path.basename(graph_file1.name)
    filename2 = os.path.basename(graph_file2.name)
    edges1 = ast.literal_eval(graph_file1.readline())
    edges2 = ast.literal_eval(graph_file2.readline())
    n1 = int(len(edges1) * 2 / 3)
    n2 = int(len(edges2) * 2 / 3)

    s2 = datetime.datetime.now()
    created_graphs = edge_split.edge_split(edges1, edges2)
    e2 = datetime.datetime.now()

    print(f"{graph_utils.timestamp()}    {len(created_graphs)} graphs created in {graph_utils.time_diff(s2, e2)}")

    edge_split.simulate_zf(created_graphs, n1 + n2 + 2, filename1, filename2, results_dir_path)
    e1 = datetime.datetime.now()

    print(f"{graph_utils.timestamp()} Finished in {graph_utils.time_diff(s1, e1)}")


def select_dir():

    # Asking for save directory
    return filedialog.askdirectory()


def select_files_itself():

    # Asking for graphs to simulate edge splitting on
    files = filedialog.askopenfilenames()
    print(f"{graph_utils.timestamp()} Selected {len(files)} graphs")

    return files


def select_files_other():

    # Asking for graphs to simulate edge splitting on
    file1 = filedialog.askopenfilename()
    file2 = filedialog.askopenfilename()
    print(f"{graph_utils.timestamp()} Selected 2 graphs to edge split together")

    return file1, file2


print("Edge splitting with itself or with other graphs? (i/o)")
ans = input()

if ans.lower() == "i":
    edge_split_itself()
    input()

elif ans.lower() == "o":
    edge_split_other()
    input()

else:
    print("Invalid input - Press enter to exit!")
    input()
