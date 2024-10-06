import random
import time
import matplotlib.pyplot as plt
import networkx as nx

from main import UnionFind, SetNode


class WeightedGraph:
    def __init__(self, nodes=0):
        self.adj_list: dict[SetNode, list[SetNode]] = {SetNode(node, header=None): [] for node in range(nodes)}
        self.nodes = list(self.adj_list.keys())
        self.adj_matrix = None
        self.weights = {}

    def add_node(self):
        new_node = SetNode(self.nodes[-1].cargo + 1, header=None)
        self.adj_list[new_node] = []
        self.nodes.append(new_node)

    def add_edge(self, node1, node2, weight):
        if node1 in self.adj_list and node2 in self.adj_list:
            self.adj_list[node1].append(node2)
            self.adj_list[node2].append(node1)
            self.weights[(node1, node2)] = weight
            self.weights[(node2, node1)] = weight

    def kruskal_mst(self):
        edges = []

        for (node1, node2), weight in self.weights.items():
            if (weight, node1, node2) not in edges and (weight, node2, node1) not in edges:
                edges.append((weight, node1, node2))

        edges.sort(key=lambda edge: edge[0])

        uf = UnionFind()
        for node in self.nodes:
            uf.make_set(node)
        mst = []
        mst_weight = 0

        start_time = time.time()

        for weight, node1, node2 in edges:
            root1 = uf.find(node1)
            root2 = uf.find(node2)

            if root1 != root2:
                uf.union(node1, node2)
                mst.append((node1, node2, weight))
                mst_weight += weight

        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"{elapsed_time:.10f}")

        return mst, mst_weight

    def visualize(self):
        graph = nx.Graph()
        for node in self.nodes:
            graph.add_node(node.cargo)
        for (node1, node2), weight in self.weights.items():
            if node1.cargo < node2.cargo:
                graph.add_edge(node1.cargo, node2.cargo, weight=weight)
        pos = nx.spring_layout(graph)
        plt.figure(figsize=(8, 6))
        nx.draw(graph, pos, with_labels=True, node_color='red', node_size=700, font_size=14, font_color='black',
                edge_color='gray')
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='blue')
        plt.show()

    def visualize_mst(self, mst):
        mst_graph = nx.Graph()
        for node in self.nodes:
            mst_graph.add_node(node.cargo)
        for node1, node2, weight in mst:
            mst_graph.add_edge(node1.cargo, node2.cargo, weight=weight)
        pos = nx.spring_layout(mst_graph)
        plt.figure(figsize=(10, 8))
        nx.draw(mst_graph, pos, with_labels=True, node_color='blue', node_size=700, font_size=14, font_color='white',
                edge_color='green')
        edge_labels = {(node1.cargo, node2.cargo): weight for node1, node2, weight in mst}
        nx.draw_networkx_edge_labels(mst_graph, pos, edge_labels=edge_labels, font_color='red')
        plt.show()

    @classmethod
    def generate_random_graph(cls, n, p, weight_range=(1, 10)):
        graph = cls(n)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    weight = random.randint(weight_range[0], weight_range[1])
                    graph.add_edge(graph.nodes[i], graph.nodes[j], weight)
        return graph


g = WeightedGraph.generate_random_graph(10, 0.4)
g.visualize()
g.visualize_mst(g.kruskal_mst()[0])
