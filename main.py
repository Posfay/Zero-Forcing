import networkx as nx
import subset_generating
import zero_forcing
import graph_utils
import zero_forcing_process as zf


# set_1 = [1, 2, 3, 4, 5, 6]
# subset_generating.process_subsets(set_1, 4)
#
# G = nx.Graph()
#
# G.add_node(0, b=0)
# G.add_node(1, b=0)
# G.add_node(2, b=0)
# G.add_node(3, b=1)
#
# G.add_edge(0, 1)
# G.add_edge(1, 2)
# G.add_edge(2, 3)
#
# zero_forcing.simulate_zero_forcing(G)
#
# graph_utils.draw_nx_graph(graph_utils.generate_3_regular_graph(20))

graphs = zf.generate_graphs(12)
zf_number = zf.simulate_zero_forcing_on_graphs(graphs)
