import zero_forcing_process as zf


graph, initial_black_nodes_list = zf.generate_initial_coloring(6)
zf_number = zf.simulate_zero_forcing_on_graph(graph, initial_black_nodes_list)
