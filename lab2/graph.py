import numpy as np
import random
import matplotlib.pyplot as plt
import networkx as nx


__all__ = ('Graph', 'DirectedGraph', 'WeightedGraph',)


class Node:

    def __init__(self, index, data=None):
        self.data = data
        self.index = index

    def __str__(self):
        return f"Node {self.index}"

    def __repr__(self):
        return f"Node {self.index}"


class Graph:
    """
    This class represents undirected graph
    """
    def __init__(self, nodes=0):
        self.adj_list: dict[Node, list[Node]] = {Node(node): [] for node in range(nodes)}
        self.nodes = list(self.adj_list.keys())
        self.adj_matrix = None

    def get_node(self, index):
        return self.nodes[index]

    def add_node(self):
        new_node = Node(self.nodes[-1].index + 1)
        self.adj_list[new_node] = []
        self.nodes.append(new_node)

    def add_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)

    def remove_node(self, node):
        if node in self.adj_list:
            for n in self.adj_list:
                if node in self.adj_list[n]:
                    self.adj_list[n].remove(node)
            del self.adj_list[node]
            self.nodes.remove(node)

    def remove_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            if node2 in self.adj_list[node1]:
                self.adj_list[node1].remove(node2)
            if node1 in self.adj_list[node2]:
                self.adj_list[node2].remove(node1)

    def covert_to_adj_matrix(self):
        n = len(self.nodes)
        self.adj_matrix = np.zeros((n, n), dtype=int)

        for node in self.nodes:
            for neighbor in self.adj_list[node]:
                self.adj_matrix[node.index][neighbor.index] = 1
                self.adj_matrix[neighbor.index][node.index] = 1

    def visualize(self) -> None:
        graph = nx.Graph()
        for node in self.nodes:
            graph.add_node(node.index)
        for node, neighbors in self.adj_list.items():
            for neighbor in neighbors:
                graph.add_edge(node.index, neighbor.index)

        plt.figure(figsize=(8, 6))
        nx.draw(graph, with_labels=True, node_color='red', node_size=700, font_size=14, font_color='black',
                edge_color='gray')
        plt.show()

    @classmethod
    def generate_random_graph(cls, n, p):
        graph = cls(n)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    graph.add_edge(graph.nodes[i], graph.nodes[j])
        return graph


class DirectedGraph(Graph):
    """
    This class represents a directed graph
    """
    def __init__(self, nodes=0):
        super().__init__(nodes)

    def add_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)

    def remove_edge(self, node1, node2):
        if node1 in self.adj_list and node2 in self.adj_list:
            if node2 in self.adj_list[node1]:
                self.adj_list[node1].remove(node2)

    def covert_to_adj_matrix(self):
        n = len(self.nodes)
        self.adj_matrix = np.zeros((n, n), dtype=int)

        for node in self.nodes:
            for neighbor in self.adj_list[node]:
                self.adj_matrix[node.index][neighbor.index] = 1

    @classmethod
    def generate_random_graph(cls, n, p):
        graph = cls(n)
        for i in range(n):
            for j in range(n):
                if i != j and random.random() < p:
                    graph.add_edge(graph.nodes[i], graph.nodes[j])
        return graph


class WeightedGraph(DirectedGraph):
    def __init__(self, nodes=0):
        super().__init__(nodes)
        self.adj_list: dict[Node, list[tuple[Node, int]]]

    def add_edge(self, node1, node2, weight):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append((node2, weight))

    def remove_edge(self, node1, node2):
        if node1 in self.adj_list:
            self.adj_list[node1] = [edge for edge in self.adj_list[node1] if edge[0] != node2]

    def covert_to_adj_matrix(self):
        n = len(self.nodes)
        self.adj_matrix = np.zeros((n, n), dtype=float)

        for node in self.nodes:
            for neighbor, weight in self.adj_list[node]:
                self.adj_matrix[node.index][neighbor.index] = weight

    @classmethod
    def generate_random_graph(cls, n: int, p: int, w_limit: (int, int)):
        graph = cls(n)
        min_weight, max_weight = w_limit
        for i in range(n):
            for j in range(n):
                if i != j and random.random() < p:
                    weight = random.randint(min_weight, max_weight)
                    graph.add_edge(graph.nodes[i], graph.nodes[j])
                    graph.adj_list[graph.nodes[i]].append((graph.nodes[j], weight))
        return graph
