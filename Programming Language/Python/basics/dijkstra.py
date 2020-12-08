# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 19:32:24 2020

@author: ikr
"""
#NetworkX is a Python library for studying graphs and networks.
import networkx as nx
import matplotlib.pyplot as plt

#for undirected graph
#G = nx.Graph()
#for directed graph
G = nx.DiGraph()

edges = [("a", "b", 10), ("a", "c", 3), 
         ("b", "c", 1), ("b", "d", 2), 
         ("c", "b", 4), ("c", "d", 8), ("c", "e", 2),
         ("d", "e", 7),
         ("e", "d", 9)]

e = {
    "a": {"b":10, "c":3},
    "b": {"c":1, "d":2},
    "c": {"b":4, "d":8, "e":2},
    "d": {"e":7},
    "e": {"d":9}     
}


G.add_weighted_edges_from(edges)

#shortest path
shortestPath = nx.dijkstra_path(G, "a", "d")
print(f"Shortest path -> {shortestPath}")

#shortest distance
shortest_distance = nx.dijkstra_path_length(G, "a", "d")
print(shortest_distance)

# number of nodes and edges
print(G.number_of_edges(), G.number_of_nodes())


#visualize graph
#Position of nodes using Fruchterman-Reingold force-directed algorithm.
pos = nx.spring_layout(G)
weight = nx.get_edge_attributes(G, "weight")
nx.draw_networkx(G, pos, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
plt.show()