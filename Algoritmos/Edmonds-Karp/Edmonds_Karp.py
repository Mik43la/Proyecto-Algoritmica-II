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
        G.clear()

        for ind in range(len(path)):
            if path[ind] is not -1:
                G.add_edge(ind,path[ind])

        pos = nx.kamada_kawai_layout(G)
        nx.draw_networkx(G,pos)
        nx.draw(G,pos, with_labels= True)
            
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

print(maxFlow(1,8))
