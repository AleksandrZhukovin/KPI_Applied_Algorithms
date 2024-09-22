from graph import *


graph = Graph(10)
node_2 = graph.get_node(2)
node_5 = graph.get_node(5)
node_3 = graph.get_node(3)
graph.add_edge(node_2, node_5)
graph.add_edge(node_2, node_3)
graph.visualize()