
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,vis,v,stk):
        vis[v]=True
        for j in self.graph[v]:
            if vis[j]==False:
                self.dfs(vis,j,stk)

        stk.append(v)

    def topologicalSort(self):
        vis=[False]*self.V
        stk=[]
        for i in range(self.V):
            if vis[i]==False:
                self.dfs(vis,i,stk)

        print(stk[::-1]) 

g = Graph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
g.topologicalSort()

