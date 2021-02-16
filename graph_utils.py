import os
import sys
import datetime
import ast
import networkx as nx

"""
Utility functions for graph operations
"""


def write_graph_to_file(graph, zero_forcing_number, initial_black_nodes, core_path):
    """
    Saving edge list and zero forcing initial nodes list

    :param graph: Graph
    :param zero_forcing_number: int
    :param initial_black_nodes: list(int)
    :param core_path: str
    """
    nodes = graph.number_of_nodes()

    try:
        # Create dir for graph
        os.makedirs(core_path)
    except:
        # If dir exists already, skip
        pass

    file_path = f"\\{zero_forcing_number}_zf_{nodes}_nodes_"
    t = datetime.datetime.now()
    time_stamp = f"{t.strftime('%Y-%m-%d_%H-%M-%S.%f')}"
    extension = ".txt"
    final_file_path = core_path + file_path + time_stamp + extension

    file = open(final_file_path, "w")

    file.write(str(list(graph.edges)) + "\n")
    file.write(str(initial_black_nodes) + "\n")

    file.close()


def is_isomorphic_with_any(graph, zero_forcing_number, core_path):
    """
    Checking whether graph is isomorphic with any already generated ones

    :param graph: Graph
    :param zero_forcing_number: int
    :param core_path: str
    :return: bool
    """
    nodes = graph.number_of_nodes()
    dir_path = f"\\{nodes}"
    final_dir_path = core_path + dir_path

    for e in os.scandir(final_dir_path):
        # Found a graph
        if e.is_file():
            # Getting zero forcing number
            zf = int(e.name[0])
            if e.name[1].isnumeric():
                # If zero forcing number is 2 digits
                zf = int(e.name[0:2])
            if zf == zero_forcing_number:
                file = open(e.path, "r")
                edge_list = ast.literal_eval(file.readline())
                g2 = nx.Graph()
                g2.add_edges_from(edge_list)
                if nx.is_isomorphic(graph, g2):
                    return True

    return False


def timestamp():
    """
    Creating a human-friendly timestamp

    :return: str
    """
    t = datetime.datetime.now()
    return f"[{t.strftime('%d/%m - %H:%M:%S')}]"


def time_diff(t1, t2):
    """
    Calculating the difference in time between two datetime objects

    :param t1: datetime
    :param t2: datetime
    :return: str
    """
    diff = t2 - t1
    sec = diff.total_seconds()
    one_day = 60 * 60 * 24
    one_hour = 60 * 60
    one_minute = 60
    if sec >= one_day:
        d = sec // one_day
        h = (sec % one_day) // one_hour
        return f"{round(d)}d {round(h)}h"
    elif sec >= one_hour:
        h = sec // one_hour
        m = (sec % one_hour) // one_minute
        return f"{round(h)}h {round(m)}m"
    elif sec >= one_minute:
        m = sec // one_minute
        s = sec % one_minute
        return f"{round(m)}m {round(s)}s"
    else:
        return f"{sec}s"
