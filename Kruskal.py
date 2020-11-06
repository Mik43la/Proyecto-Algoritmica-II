import ast

import networkx as nx
import matplotlib.pyplot as plt

global G, destino, labls2


class Graph:
    global G, destino, labls2

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

        result = []  # MST
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1 and i < len(self.graph):

            u, v, w = self.graph[i]
            i = i + 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        # for i in range(len(result)):
        #     if self.find(parent,result[i][0]) == self.find(parent, destino):
        #         ruta.append(result[i])

        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            G.add_edge(u, v, weight=weight)
            G[u][v]['weight'] = weight

            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
        # print(len(result), len(ruta))


def main():
    global G, destino, labls2
    destino = 20

    G = nx.Graph()

    rf = open("lugares.txt", "r")
    cities = ast.literal_eval(rf.read())
    rf.close()
    rf = open("coordenadas.txt", "r")
    pos = ast.literal_eval(rf.read())
    rf.close()

    rf = open("connections.txt", "r")

    n, m = map(int, rf.readline().split())

    g = Graph(n + 1)  # n+1 para que los txt coincidan

    for i in range(m):
        a, b, peso = map(float, rf.readline().split())
        g.addEdge(int(a), int(b), peso)
        g.addEdge(int(b), int(a), peso)

    g.KruskalMST()

    img = plt.imread("MapaCarreteraBolivia.PNG")
    fig, ax = plt.subplots(figsize=(15, 15))

    ax.imshow(img, extent=[-150, 200, -150, 200], alpha=0.7)

    list_of_nodes = list(G.nodes())
    #
    new_dict = "{"
    new_pos = "{"

    for i in range(G.number_of_nodes()):
        new_dict += str(list_of_nodes[i]) + ':"' + str(cities.get(list_of_nodes[i])) + '",'
        new_pos += "\"" + str(cities.get(list_of_nodes[i])) + "\":" + str(pos.get(cities.get(list_of_nodes[i]))) + ','

    new_dict += "}"
    new_pos += '}'

    dicty = ast.literal_eval(new_dict)
    poss = ast.literal_eval(new_pos)

    nx.relabel_nodes(G, mapping=dicty, copy=False)

    labels = nx.get_edge_attributes(G, 'weight')

    list_of_edges = list(G.edges())
    new_labels = "{"

    for i in range(len(list_of_edges)):
        new_labels += str(list_of_edges[i]) + ': ' + str(labels.get(list_of_edges[i])) + ', '

    new_labels += "}"

    labls2 = ast.literal_eval(new_labels)

    G.remove_node('None')

    nx.draw_networkx(G, poss, with_labels=True, node_color="cyan", node_size=80, width=1)

    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(G, poss, edge_labels=labels)
    plt.savefig("path_Kruskal.png")

    #plt.show()

