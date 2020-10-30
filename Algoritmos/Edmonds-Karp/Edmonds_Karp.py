import ast
import networkx as nx
import matplotlib.pyplot as plt
INF = 100000001
MAX_N = 10
grafo = [[-1]* MAX_N for i in range(MAX_N)]


# s = source, t = sink
def maxFlow(s,t):
    maxFlow = 0

    while(True):

        path = [-1] * MAX_N
        queue = []

        queue.insert(0,s)
        path[s] = s

        while(len(queue) is not 0 and path[t] == -1):
            currentNode = queue.pop(0)

            for i in range(MAX_N):
                if path[i] is -1 and (grafo[currentNode][i] > 0):
                    path[i] = currentNode
                    queue.insert(0,i)

        minFlow = INF

        if path[t] == -1:
            break

        from_n = path[t]
        to = t
        while(from_n != to):
            minFlow = min(minFlow, grafo[from_n][to])
            to = from_n
            from_n = path[to]

        from_n = path[t]
        to = t
        while(from_n != to):
            grafo[to][from_n] += minFlow
            grafo[from_n][to] -= minFlow
            to = from_n
            from_n = path[to]

        maxFlow += minFlow
        print(path)
        rf = open("coordinates.txt", "r")
        pos = ast.literal_eval(rf.read())
        rf = open("cities.txt", "r")
        cities = ast.literal_eval(rf.read())

        for ind in range(len(path)):
            if path[ind] is not -1:
                G.add_edge(ind,path[ind])
        nx.relabel_nodes(G, cities, copy= False)

        rf.close()

        img = plt.imread("mapBolivia.jpg")
        fig, ax = plt.subplots(figsize=(15, 15))
        
        ax.imshow(img, extent=[-100, 10, -100, 10])

        nx.draw_networkx(G,pos)

        plt.show()
        G.clear()


    return maxFlow


G = nx.Graph()

rf = open("text.txt", "r")

n, m = map(int, rf.readline().split())

for i in range(m):
    a, b, capacity = map(int, rf.readline().split())
    grafo[a][b] = capacity
    grafo[b][a] = 0

print(maxFlow(0,8))

