from collections import deque, namedtuple
import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq
import math

class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary

    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def KruskalMST(self):

        result = []  #  MST
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []


        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:


            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)


            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)


        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            G.add_edge(u,v,weight=weight)
            G[u][v]['weight']=weight

            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


G = nx.Graph()

rf = open("text.txt", "r")

n, m = map(int, rf.readline().split())

g = Graph(n)
for i in range(m):
    a, b, peso = map(int, rf.readline().split())
    g.addEdge(a,b,peso)


g.KruskalMST()
pos=nx.circular_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
