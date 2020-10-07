import networkx as nx
import subset_generating
import zero_forcing
import graph_utils
import zero_forcing_process as zf


graphs = zf.generate_graphs(12)
zf_number = zf.simulate_zero_forcing_on_graphs(graphs)
