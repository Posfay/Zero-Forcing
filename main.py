import os
import sys
import time
import zero_forcing_process as zf
import graph_utils


def print_results():

    now_time = time.time()
    diff_time_in_sec = now_time - start_time
    generated_per_second = total / diff_time_in_sec
    generated_per_hour = 3600 * generated_per_second
    saved_per_second = success / diff_time_in_sec
    saved_per_hour = 3600 * saved_per_second

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'Generated:' : <16}{total : <12}")
    print(f"{'New graphs:' : <16}{success : <12}")
    print(f"{'Success rate:' : <16}{round((success / total) * 100, 3) : <7} %")
    print(f"{'Speed:' : <16}{round(generated_per_hour) : <7} graphs/h")
    print(f"{'Save speed:' : <16}{round(saved_per_hour) : <7} graphs/h")


nodes = int(sys.argv[1])
total = 0
success = 0
one_min_total = 0
start_time = time.time()

while True:
    total += 1

    graph, initial_black_nodes_list = zf.generate_initial_coloring(nodes)
    zf_number, init_black_nodes_successful = zf.simulate_zero_forcing_on_graph(graph, initial_black_nodes_list)
    if ((zf_number / nodes) > (1/3)) and (not graph_utils.is_isomorphic_with_any(graph, zf_number)):
        graph_utils.write_graph_to_file(graph, zf_number, init_black_nodes_successful)
        success += 1

    if nodes <= 12:
        if total % 10 == 0:
            print_results()
    else:
        print_results()
