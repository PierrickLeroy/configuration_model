"""
A module for the barabasi-albert model
"""

import numpy as np

def generate_edgeList(G, m, N, intermediate_steps=None, A=0):
    """Generates a list of edges from an initial graph G following the BA model.
    Source : https://en.wikipedia.org/wiki/Barabási–Albert_model

    Args:
        G (nx.Graph): initial graph
        m (int): degree of arriving nodes
        N (int): number of nodes to add to G
        intermediate_steps (list): intermediate states of the BA model

    Returns:
        list: tuples (v1, v2) representing edges to add to G stored in a list
    """
    if intermediate_steps is not None:
        states = []
    degrees = [deg for node, deg in G.degree]
    sum_degrees = sum(degrees)
    m_0 = G.number_of_nodes()
    edge_list = []
    node_list = list(np.arange(m_0))

    for i in range(m_0, N+m_0):
        a = np.random.choice(node_list, m, p=(np.array(degrees))/sum_degrees, replace=False)
        for x in a:
            degrees[x] += 1
            edge_list.append((x, i))
        degrees.append(m)
        node_list.append(i)
        sum_degrees += 2*m
        if intermediate_steps is not None and i in intermediate_steps:
            states.append(edge_list.copy())
    return edge_list, states if intermediate_steps is not None else edge_list
