from collections import deque, namedtuple
import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq
import math
import heapq

INF = 100000010
SIZE = 100000 + 1
distances = [INF] * SIZE
visited = [False] * SIZE
vertex = [[] for i in range(SIZE)]
road = [0] * SIZE
cities = {0:"La Paz",1:"Santa Cruz",2:"Cochabamba",3:"Sucre",4:"Oruro",5:"Tarija",6:"Beni",7:"Potosi",8:"Pando"}
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
cities = {0:"La Paz",1:"Santa Cruz",2:"Cochabamba",3:"Sucre",4:"Oruro",5:"Tarija",6:"Beni",7:"Potosi",8:"Pando"}

n, m = map(int, rf.readline().split())

for i in range(m):
    a, b, peso = map(int, rf.readline().split())

    vertex[a].append((peso, b))

    vertex[b].append((peso, a))

dijkstra(4)

for i in range(1, n + 1):
    print('[ ', end='')
    print(distances[i], end=' ]')

for i in range(1, n + 1):
    G.add_edge(i, road[i], weight=distances[i])
    G[i][road[i]]['weight'] = distances[i]

G = nx.relabel_nodes(G, cities, copy=False)
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos, node_color="cyan", node_size=1050, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

rf.close()
