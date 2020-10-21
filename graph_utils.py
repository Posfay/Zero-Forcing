import sys
import datetime

"""
Utility functions for graph operations
"""


# Path of folder which contains "Graphs" folder
# eg. "D:\myfiles\Zero-Forcing" -> no \ at the end
core_path = sys.argv[2]


def write_graph_to_file(graph, zero_forcing_number, initial_black_nodes):

    nodes = graph.number_of_nodes()
    file_path = f"\\Graphs\\{nodes}\\{zero_forcing_number}_zf_{nodes}_nodes_"
    t = datetime.datetime.now()
    time_stamp = f"{t.strftime('%Y')}-{t.strftime('%m')}-" \
                 f"{t.strftime('%d')}_{t.strftime('%H')}-" \
                 f"{t.strftime('%M')}-{t.strftime('%S')}." \
                 f"{t.strftime('%f')}"
    extension = ".txt"
    final_file_path = core_path + file_path + time_stamp + extension

    file = open(final_file_path, "w")

    file.write(str(list(graph.edges)) + "\n")
    file.write(str(initial_black_nodes) + "\n")

    file.close()
