INF=999999999
graph=[[INF, 1, 2, 5, INF, INF, INF, INF],  
         [INF, INF, INF, INF, 4, 11, INF, INF],  
         [INF, INF, INF, INF, 9, 5, 16, INF],  
         [INF, INF, INF, INF, INF, INF, 2, INF],  
         [INF, INF, INF, INF, INF, INF, INF, 18], 
         [INF, INF, INF, INF, INF, INF, INF, 13],  
         [INF, INF, INF, INF, INF, INF, INF, 2],
         [INF, INF, INF, INF, INF, INF, INF, INF]]

target=6
N=8

def fun(graph,vertex):
    if (vertex==target):
        return 0
     
    minimum=999999999
    for i in range(N):
        if graph[vertex][i]==INF or graph[vertex][i]==0:
            continue
        minimum= min(minimum,graph[vertex][i]+fun(graph,i))
    return minimum

print(fun(graph,1))
