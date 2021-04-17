import os
import ast
import datetime
import tkinter as tk
from tkinter import filedialog
import pendant_injection
import graph_utils


root = tk.Tk()
root.withdraw()


def pendant_injection_in_directory():

    results_dir_path = select_dir()
    files = select_files()

    s1 = datetime.datetime.now()
    c = 0
    for file in files:
        s2 = datetime.datetime.now()
        graph_file = open(file, "r")
        filename = os.path.basename(graph_file.name)
        edges = ast.literal_eval(graph_file.readline())
        zf_edges = ast.literal_eval(graph_file.readline())
        zfn = len(zf_edges)
        n = int(len(edges) * 2 / 3)
        c += 1

        # Checking if graph has already been processed
        if processed_graph_before(results_dir_path, filename):
            print(f"{graph_utils.timestamp()} Graph {c}/{len(files)} has already been processed")
            continue

        s3 = datetime.datetime.now()
        created_graphs = pendant_injection.inject_pendants(edges)
        e3 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()}    {len(created_graphs)} graphs created in {graph_utils.time_diff(s3, e3)}")
        pendant_injection.simulate_zf(created_graphs, n + 6, zfn, filename, results_dir_path)

        e2 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()} {c}/{len(files)} finished in {graph_utils.time_diff(s2, e2)}")
    e1 = datetime.datetime.now()
    print()
    print(f"{graph_utils.timestamp()} Total run time: {graph_utils.time_diff(s1, e1)}")


def processed_graph_before(results_core_path, graph_name):
    """
    Checks whether a given graph has already been processed by pendant injection

    :param results_core_path: str
    :param graph_name: str
    :return: bool
    """
    processed_dir_path = f"{results_core_path}\\Processed Graphs"

    # No graphs has been processed
    if not os.path.exists(processed_dir_path):
        return False

    processed_graphs = os.listdir(processed_dir_path)

    if graph_name in processed_graphs:
        return True
    else:
        return False


def select_dir():
    # Asking for save directory
    return filedialog.askdirectory()


def select_files():
    # Asking for graphs to simulate pendant injection on
    files = filedialog.askopenfilenames()
    print(f"{graph_utils.timestamp()} Selected {len(files)} graphs")

    return files


print("Select a directory for the results and the files to do the pendant injection on")
pendant_injection_in_directory()
input()
