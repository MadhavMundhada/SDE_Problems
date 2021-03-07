
from collections import defaultdict

def bfs(s):
    visited=[False]*y
    q=[]
    q.append(s)

    visited[s]=True
    #print(q)
    while q:
        s=q.pop(0)
        print(s,end=" ")
        for i in graph[s]:
            
            if visited[i]==False:
                q.append(i)
                visited[i]=True


graph=defaultdict(list)
y, k = map(int,input().split())

for __ in range(k):

    
    t, m =map(int,input().split())
    graph[t].append(m)
    graph[m].append(t) 
    
print(graph)
bfs(int(input()))





        
