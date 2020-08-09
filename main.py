import networkx as nx
import subset_generating
import zero_forcing


# set_1 = [1, 2, 3, 4, 5, 6]
# subset_generating.process_subsets(set_1, 4)

G = nx.Graph()

G.add_node(0, b=0)
G.add_node(1, b=0)
G.add_node(2, b=0)
G.add_node(3, b=1)

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)

zero_forcing.simulate_zero_forcing(G)
