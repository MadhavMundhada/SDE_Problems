from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSRec(self,v, visited,parent):
        visited[v] = True
        for j in self.graph[v]:
            if visited[j] == False:
                if (self.DFSRec(j, visited,v)==True):
                    return True
            elif j!=parent:
                return True
        return False

    def DFS(self):
        V = len(self.graph)
        visited = [False] * V
        for i in range(V):
            if visited[i] == False:
                if (self.DFSRec(i, visited,0)==True):
                    return True
        return False


                

g = Graph()
g1=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.DFS())
#for graphs that are not connected
g1.addEdge(0,1)
g1.addEdge(1,2)
g1.addEdge(2,0)
print(g1.DFS())
