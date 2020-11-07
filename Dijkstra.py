import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import ast


INF = 100000010
SIZE = 100000 + 1
distances = [INF] * SIZE
visited = [False] * SIZE
vertex = [[] for i in range(SIZE)]
road = [0] * SIZE


destiny = 30 ####

global G


def dijkstra(initialNode):
    global G

    distances[initialNode] = 0
    s = [(0,initialNode)]

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
def main():
    global G

    rf = open("copyLugares.txt", "r")
    cities = ast.literal_eval(rf.read())
    rf.close()

    rf = open("copyCoords.txt", "r")
    pos = ast.literal_eval(rf.read())
    rf.close()

    G = nx.Graph()
    #rf = open("copyconnect.txt", "r")
   # d = rf.read()
   # print("lol")
   # print(d)
    rf = open("copyconnect.txt", "r")
    p = rf.read()
    print(p)
    rf = open("copyconnect.txt", "r")
    n, m = map(int, rf.readline().split())
    #print(m)
    for i in range(m):
        a, b, peso = map(float, rf.readline().split())
        #print(a,b,peso)
        vertex[int(a)].append((peso, int(b)))
        vertex[int(b)].append((peso, int(a)))

    node = 10  # De donde empieza

    dijkstra(node)

    for i in range(0, n + 1):
        print('[ ', end='')
        print(distances[i], end=' ]')

    print()

    i = destiny
    while (i is not node):
        print(road[i], end=" ")
        formatted_weight = "{:.2f}".format(distances[i])
        G.add_edge(road[i], i, weight=formatted_weight)

        G[road[i]][i]['weight'] = formatted_weight
        i = road[i]

    img = plt.imread("MapaCarreteraBolivia.PNG")
    fig, ax = plt.subplots(figsize=(15, 15))

    ax.imshow(img, extent=[-150, 200, -150, 200], alpha=0.7, resample=False)

    list_of_nodes = list(G.nodes())

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

    # G.remove_node('None')

    nx.draw_networkx(G, poss, with_labels=True, node_color="cyan", node_size=80, width=1)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, poss, edge_labels=labels, font_size=7)

    plt.savefig("path_Dijkstra.png")

    #plt.show()

    rf.close()
