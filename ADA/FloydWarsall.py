

V = int(input("ENTER THE NUMBER OF VERTICES IN THE GRAPH"))
INF = 9999999999


def floydWarshall(graph):

    dist = map(lambda i: map(lambda j: j, i), graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Agr vertex k ,I se J tk ka shortest path me hai fhir usko dist[i][j] se update karo
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)


def printSolution(dist):
    print(" the shortest distances  between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF")),
            else:
                print("%7d\t" % (dist[i][j])),
            if j == V-1:
                print("")


graph = [[0, 20, INF, 73],
         [INF, 0, 56, INF],
         [INF, INF, 0, 22],
         [INF, INF, INF, 0]
         ]

floydWarshall(graph)
