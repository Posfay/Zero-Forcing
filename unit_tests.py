import networkx as nx
import subset_generating
import zero_forcing


def edge_graph():

    g = nx.Graph()
    g.add_nodes_from(range(2))
    g.add_edge(0, 1)
    return g


def triangle_graph():

    g = nx.Graph()
    g.add_nodes_from(range(3))
    g.add_edges_from([(0, 1), (1, 2), (2, 0)])
    return g


def square_graph():

    g = nx.Graph()
    g.add_nodes_from(range(4))
    g.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])
    return g


def cycle_6_graph():

    g = nx.Graph()
    g.add_nodes_from(range(6))
    g.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
    return g


def test_subset_generating():

    assert subset_generating.process_subsets([1], 0) == [[]]
    assert subset_generating.process_subsets([1], 1) == [[1]]
    assert subset_generating.process_subsets([1, 2, 3], 1) == [[1], [2], [3]]
    assert subset_generating.process_subsets([1, 2, 3], 2) == [[1, 2], [1, 3], [2, 3]]
    assert subset_generating.process_subsets([1, 2, 3], 3) == [[1, 2, 3]]


def test_simulate_zero_forcing():

    eg = edge_graph()
    tg = triangle_graph()
    sg = square_graph()
    cg = cycle_6_graph()

    assert zero_forcing.simulate_zero_forcing(eg, [0]) == (1, True)
    assert zero_forcing.simulate_zero_forcing(tg, [1, 2]) == (2, True)
    assert zero_forcing.simulate_zero_forcing(sg, [2, 3]) == (2, True)
    assert zero_forcing.simulate_zero_forcing(cg, [0, 1]) == (2, True)

    assert zero_forcing.simulate_zero_forcing(eg, []) == (0, False)
    assert zero_forcing.simulate_zero_forcing(tg, [2]) == (1, False)
    assert zero_forcing.simulate_zero_forcing(sg, [0, 2]) == (2, False)
    assert zero_forcing.simulate_zero_forcing(cg, [1]) == (1, False)
