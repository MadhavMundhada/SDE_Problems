from collections import defaultdict
def dfsrecurr(visited,v):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        #print("recurr",i)
        if visited[i]==False:
            dfsrecurr(visited,i)
            
graph=defaultdict(list)
y, k = map(int,input().split())

for __ in range(k):

    
    t, m =map(int,input().split())
    graph[t].append(m)
print(graph)
visited=[False]*y
dfsrecurr(visited,int(input()))


"""
5 12
0 1
0 2
1 0
1 3 
1 4
2 0
2 3
3 1
3 2
4 1
4 3
3 4
0
"""
