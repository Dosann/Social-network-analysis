import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def highlight_top_central_nodes(network, central_nodes, default_node_size=10, highlighted_node_size=500, default_node_color='#1F78B4', highlighted_node_color='#F44336'):
    """
    Draw network with highlighted top central nodes
    
    Arguments:
    network : graph
    central_nodes : list of central nodes to highlight in a graph
    default_node_size : default node size of non-highlighted nodes
    highlighted_node_size: size of highlighted top nodes
    default_node_color: default node color of non-highlighted nodes
    highlighted_node_color: color of highlighted top nodes
    """
    
    node_sizes = np.array([default_node_size] * network.number_of_nodes())
    node_sizes[central_nodes] = highlighted_node_size
    
    node_colors = np.array([default_node_color] * network.number_of_nodes())
    node_colors[central_nodes] = highlighted_node_color
    
    plt.figure(figsize=(20,20))
    nx.draw_networkx(network, pos=sp, with_labels=False, node_size=node_sizes, node_color=node_colors)
    plt.show()
