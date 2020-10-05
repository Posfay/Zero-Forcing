import pytest
import networkx as nx
import subset_generating
import zero_forcing
import graph_utils
import zero_forcing_process as zf


def edge_graph():

    g = nx.Graph()
    for i in range(0, 2):
        g.add_node(i)
        g.nodes[i]['b'] = 0
    g.nodes[0]['b'] = 1
    g.add_edge(0, 1)
    return g


def triangle_graph():

    g = nx.Graph()
    for i in range(0, 3):
        g.add_node(i)
        g.nodes[i]['b'] = 1
    g.nodes[0]['b'] = 0
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    return g


def square_graph():

    g = nx.Graph()
    for i in range(0, 4):
        g.add_node(i)
        g.nodes[i]['b'] = 0
    g.nodes[2]['b'] = 1
    g.nodes[3]['b'] = 1
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(0, 2)
    return g


def cycle_6_graph():

    g = nx.Graph()
    for i in range(0, 6):
        g.add_node(i)
        g.nodes[i]['b'] = 0
    g.nodes[0]['b'] = 1
    g.nodes[1]['b'] = 1
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 0)
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

    assert zero_forcing.simulate_zero_forcing(eg) == (1, True)
    assert zero_forcing.simulate_zero_forcing(tg) == (2, True)
    assert zero_forcing.simulate_zero_forcing(sg) == (2, True)
    assert zero_forcing.simulate_zero_forcing(cg) == (2, True)

    eg.nodes[0]['b'] = 0
    tg.nodes[1]['b'] = 0
    sg.nodes[3]['b'] = 0
    sg.nodes[0]['b'] = 1
    cg.nodes[0]['b'] = 0

    assert zero_forcing.simulate_zero_forcing(eg) == (0, False)
    assert zero_forcing.simulate_zero_forcing(tg) == (1, False)
    assert zero_forcing.simulate_zero_forcing(sg) == (2, False)
    assert zero_forcing.simulate_zero_forcing(cg) == (1, False)
