from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    

    def DFSRec(self,v,visited,RecStack):
        visited[v]=True
        RecStack[v]=True
        #print(visited,RecStack)
        for j in self.graph[v]:
            #print("INSIDE LOOP",j,visited,RecStack)
            if visited[j]==False:
                if self.DFSRec(j,visited,RecStack)==True:
                    return True
            elif RecStack[j]==True:
                return True
            
           
        RecStack[v]=False
        #print("After loop",visited,RecStack)
        return False



    def DFS(self):
        visited=[False]*(len(self.graph)+1)
        RecStack=[False]*(len(self.graph)+1)
        for i in range(len(self.graph)):
            #print("Start",i)
            if visited[i]==False:
                
                if self.DFSRec(i,visited,RecStack)==True:
                    return True
            
        return False
    

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)

g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3,3)
#     
print(g.DFS())

