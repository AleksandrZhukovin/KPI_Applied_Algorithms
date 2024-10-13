from lab2.graph import Node, DirectedGraph
from collections import deque, defaultdict
import random


__all__ = (
    'ModifiedDirectedGraph',
    'dfs_sort',
    'demukron_algorithm',
)


class ModifiedDirectedGraph(DirectedGraph):
    def generate_random_dag(self, num_edges):
        for _ in range(num_edges):
            from_node, to_node = random.sample(self.nodes, 2)
            if from_node.index < to_node.index:
                self.add_edge(from_node, to_node)
            elif from_node.index > to_node.index:
                self.add_edge(to_node, from_node)


def dfs(graph: DirectedGraph, node: Node, is_visited: dict[Node: bool], stack: list):
    is_visited[node] = True
    for neighbor in graph.adj_list[node]:
        if not is_visited[neighbor]:
            dfs(graph, neighbor, is_visited, stack)
    stack.append(node)


def dfs_sort(graph: DirectedGraph):
    visited = {node: False for node in graph.nodes}
    stack = []

    for node in graph.nodes:
        if not visited[node]:
            dfs(graph, node, visited, stack)
    stack.reverse()
    return stack


def demukron_algorithm(graph):
    in_edges = {node: len(neighbours) for node, neighbours in graph.adj_list}
    zero_edges_ver = deque([node for node in graph.nodes if in_edges[node] == 0])

    levels = defaultdict(list)
    level = 0

    while zero_edges_ver:
        next_level = deque()
        while zero_edges_ver:
            node = zero_edges_ver.popleft()
            levels[level].append(node)

            for neighbor in graph.adj_list[node]:
                in_edges[neighbor] -= 1
                if in_edges[neighbor] == 0:
                    next_level.append(neighbor)

        zero_edges_ver = next_level
        level += 1

    return levels
