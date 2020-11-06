import ast
import networkx as nx
import matplotlib.pyplot as plt
import json

INF = 100000001
MAX_N = 200
grafo = [[-1] * MAX_N for i in range(MAX_N)]
flux = [0] * MAX_N  ############
global G
rf = open("copyCoords.txt", "r")
pos = ast.literal_eval(rf.read())
rf = open("copyLugares.txt", "r")
cities = ast.literal_eval(rf.read())
rf.close()

G = nx.Graph()


# s = source, t = sink
def maxFlow(s, t):
    global G
    maxFlow = 0

    while (True):
        # G.clear()
        path = [-1] * MAX_N
        queue = []

        queue.insert(0, s)
        path[s] = s

        while (len(queue) is not 0 and path[t] == -1):
            currentNode = queue.pop(0)

            for i in range(MAX_N):
                if path[i] is -1 and (grafo[currentNode][i] > 0):
                    path[i] = currentNode
                    queue.insert(0, i)

        minFlow = INF

        if path[t] == -1:
            break

        from_n = path[t]
        to = t
        while (from_n != to):
            minFlow = min(minFlow, grafo[from_n][to])
            to = from_n
            from_n = path[to]

        from_n = path[t]
        to = t
        while (from_n != to):
            grafo[to][from_n] -= minFlow
            grafo[from_n][to] -= minFlow
            to = from_n
            from_n = path[to]

        maxFlow += minFlow
        # print(path)

        for ind in range(len(path)):
            if path[ind] is not -1:
                flux[ind] = 1
                # G.add_edge(ind,path[ind])
        # print(G.edges())
    for i in range(len(flux)):
        if flux[i] is 0:
            G.add_node(i)

    return maxFlow


def main():
    global G
    rf = open("copyconnect.txt", "r")

    n, m = map(int, rf.readline().split())

    for i in range(m):
        a, b, capacity = map(float, rf.readline().split())
        grafo[int(a)][int(b)] = capacity
        grafo[int(b)][int(a)] = capacity

    print(maxFlow(0, 5))  #########
    # print(G.nodes())

    img = plt.imread("MapaCarreteraBolivia.PNG")
    fig, ax = plt.subplots(figsize=(10, 10))

    ax.imshow(img, extent=[-150, 200, -150, 200])

    list_of_nodes = list(G.nodes())

    new_dict = "{"
    new_pos = "{"

    for i in range(G.number_of_nodes()):
        new_dict += str(list_of_nodes[i]) + ':"' + str(cities.get(list_of_nodes[i])) + '",'
        new_pos += "\"" + str(cities.get(list_of_nodes[i])) + "\":" + str(pos.get(cities.get(list_of_nodes[i]))) + ','
    # print(cities.get(list_of_nodes[i]))
    new_dict += "}"
    new_pos += '}'

    dicty = ast.literal_eval(new_dict)
    poss = ast.literal_eval(new_pos)

    nx.relabel_nodes(G, dicty, copy=False)
    print(poss)

    G.remove_node('None')
    nx.draw_networkx(G, poss, node_color="cyan", node_size=80, width=1)
    # nx.draw(G,pos)
    #
    # labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G,poss,edge_labels=labels)
    #
    plt.savefig("path_Edmonds.png")

    #plt.show()