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

        s3 = datetime.datetime.now()
        created_graphs = pendant_injection.inject_pendants(edges)
        e3 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()}    {len(created_graphs)} graphs created in {graph_utils.time_diff(s3, e3)}")
        pendant_injection.simulate_zf(created_graphs, n + 6, zfn, filename, results_dir_path)

        c += 1
        e2 = datetime.datetime.now()
        print(f"{graph_utils.timestamp()} {c}/{len(files)} finished in {graph_utils.time_diff(s2, e2)}")
    e1 = datetime.datetime.now()
    print()
    print(f"{graph_utils.timestamp()} Total run time: {graph_utils.time_diff(s1, e1)}")


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
