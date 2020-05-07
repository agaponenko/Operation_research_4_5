import networkx as nx
import bellmanford as bf
import matplotlib.pyplot as plt

def init_single_source(s):
    for i in range(v):
        dist[i] = float("Inf")
        pred[i] = -1
    dist[s] = 0


def relax(u, v, w):
    if dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        pred[v] = u


def draw_graph(s, d, dist, graph):
    if str(dist[d]) == 'inf':
        print("There isn't shortest path between these vertixes.")
    else :
        length, nodes, negative_cycle = bf.bellman_ford(graph, source=s + 1, target=d + 1)
        print("Shortest path from source " + str(s) + " to destination " + str(d) + " is:", "->".join(str(n) for n in nodes))
        print("Weight: " + str(dist[d]))
        pair_nodes = [(nodes[i],nodes[i+1]) for i in range(len(nodes)-1)]
        pos = nx.shell_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='forestgreen')
        nx.draw_networkx_edges(graph, pos, width=3, alpha=0.8)
        nx.draw_networkx_edges(graph, pos, edgelist=pair_nodes, edge_color='aquamarine', width=7, alpha=0.5)
        nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif')
        plt.show()

def bellman(s):
    init_single_source(s)
    for k in range(v - 1):
        for i in range(v):
            for j in range(v):
                if g[i][j] != 0:
                    relax(i, j, g[i][j])


def path_trace(d, s):
    if d == s:
        print(str(s + 1))
    else:
        path_trace(s, pred[d])
        print(str(d + 1))



graph = nx.DiGraph()

v = int(input("Enter Number of vertices:"))

e = int(input("Enter Number of edges:"))

g = []

pred = []

dist = []

for i in range(v):
    ta = []
    pred.append(0)
    dist.append(0)
    for j in range(v):
        ta.append(0)
    g.append(ta)

for i in range(e):
    print("Edge " + str(i + 1))
    start = int(input("Start Vertex: "))
    end = int(input("End Vertex: "))
    weight = int(input("Weight: "))
    graph.add_edge(start, end, weight=weight)
    g[start - 1][end - 1] = weight

s = int(input("Source Vertex: ")) - 1
d = int(input("Destination Vertex: ")) - 1

bellman(s)
draw_graph(s,d,dist,graph)

