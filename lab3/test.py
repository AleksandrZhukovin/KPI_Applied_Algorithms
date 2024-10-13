import time
from statistics import mean
import matplotlib.pyplot as plt

from main import *


def generate_random_graph(num_nodes, edge_prob):
    graph = ModifiedDirectedGraph(num_nodes)
    num_edges = int(edge_prob * num_nodes * (num_nodes - 1) / 2)
    graph.generate_random_dag(num_edges)
    return graph


def run_with_timer(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start


num_nodes = [50, 100, 250, 500]
edge_probs = [0.3, 0.7]
iterations = 50

results = {
    "nodes": [],
    "dfs_sort_0.3": [],
    "dfs_sort_0.7": [],
    "demukron_0.3": [],
    "demukron_0.7": []
}

for num_node in num_nodes:
    for edge_prob in edge_probs:
        topological_times = []
        demukron_times = []

        for _ in range(iterations):
            graph = generate_random_graph(num_node, edge_prob)

            topological_times.append(
                run_with_timer(dfs_sort, graph)
            )
            demukron_times.append(
                run_with_timer(demukron_algorithm, graph)
            )

        avg_dfs_time = mean(topological_times)
        avg_dem_time = mean(demukron_times)

        print(f"Vertexes: {num_node}, edge prob: {edge_prob}")
        print(f"DFS Sort time: {avg_dfs_time:.10f}")
        print(f"Demukron time: {avg_dem_time:.10f}")
        print("-" * 50)

        if edge_prob == 0.3:
            results["dfs_sort_0.3"].append(avg_dfs_time)
            results["demukron_0.3"].append(avg_dem_time)
        else:
            results["dfs_sort_0.7"].append(avg_dfs_time)
            results["demukron_0.7"].append(avg_dem_time)

    results["nodes"].append(num_node)


num_node = results["nodes"]

plt.plot(num_nodes, results["dfs_sort_0.3"], label="DFS Sort (p=0.3)", marker='o')
plt.plot(num_nodes, results["dfs_sort_0.7"], label="DFS Sort (p=0.7)", marker='o')
plt.xlabel("Number of Vertexes")
plt.ylabel("Time")

plt.plot(num_nodes, results["demukron_0.3"], label="Demukron (p=0.3)", marker='o')
plt.plot(num_nodes, results["demukron_0.7"], label="Demukron (p=0.7)", marker='o')

plt.legend()

plt.tight_layout()
plt.show()
