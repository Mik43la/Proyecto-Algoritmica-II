from collections import deque, namedtuple
import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq
import math
import heapq
import ast

INF = 100000010
SIZE = 100000 + 1
distances = [INF] * SIZE
visited = [False] * SIZE
vertex = [[] for i in range(SIZE)]
road = [0] * SIZE

rf = open("cities.txt", "r")
cities =ast.literal_eval( rf.read())
rf.close()


rf = open("coordinates.txt", "r")
pos=ast.literal_eval(rf.read())
rf.close()

G = nx.Graph()


def dijkstra(initialNode):
    distances[initialNode] = 0
    s = [(0, initialNode)]

    while len(s) is not 0:

        p = s.pop()

        x = p[1]
        w = p[0]

        if visited[x] is True:
            continue
        visited[x] = True

        for i in range(len(vertex[x])):
            edge = vertex[x][i][1]
            weight = vertex[x][i][0]

            if (distances[x] + weight) < distances[edge]:
                road[edge] = x
                distances[edge] = distances[x] + weight
                s.append((distances[edge], edge))


#############
rf = open("text.txt", "r")

n, m = map(int, rf.readline().split())

for i in range(m):
    a, b, peso = map(int, rf.readline().split())

    vertex[a].append((peso, b))

    vertex[b].append((peso, a))

node = 0

dijkstra(node)

for i in range(0, n +1):

    print('[ ', end='')
    print(distances[i], end=' ]')

for a in range( n +1):
    G.add_edge(node, a, weight=distances[a])
    G[node][a]['weight'] = distances[a]

G = nx.relabel_nodes(G, cities, copy=False)

img = plt.imread("mapBolivia.jpg")
fig, ax = plt.subplots(figsize=(15,15))

ax.imshow(img, extent=[-100,10,-100,10])

nx.draw_networkx(G, pos, node_color="cyan", node_size=1050, width= 1,with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

rf.close()
