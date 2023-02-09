from scipy.stats import powerlaw
import numpy as np


def generate_degreeDistribution(gamma, N):
    return (1/powerlaw(gamma+1).rvs(size=N)).astype(int)
    
def generate_edgeList(a, allow_multilinks=False, allow_selfloops=False):
    """generates a list of edges from a degee distribution

    Args:
        a (iterable): degree distribution

    Returns:
        list: list of edges (node1, node2)
    """
    a = list(a)
    edge_list = []
    current_node = 0
    while a and np.array(a).sum() > 1:
        if a[0]==0:
            a = a[1:]
            current_node = current_node+1
        else:
            a[0] -= 1
            linked_node = np.random.choice(np.arange(len(a)), p = np.array(a)/np.array(a).sum())
            a[linked_node] -= 1
            edge_list.append([current_node, linked_node])
    
    if not allow_selfloops:
        edge_list = [[x[0], x[1]] for x in edge_list if x[0]!=x[1]]
    
    if not allow_multilinks:
        edge_list = [list(x) for x in {frozenset(x) for x in edge_list}]
    
    return edge_list