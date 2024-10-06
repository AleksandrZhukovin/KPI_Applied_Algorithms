from kruskal import WeightedGraph


for n in [150, 300, 600]:
    print(f"\n{n} vertices")
    weighted_graph = WeightedGraph.generate_random_graph(n, 0.5)
    weighted_graph.kruskal_mst()
