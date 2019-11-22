
graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],  
             [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],  
             [0, 1, 1, 1, 0], ] 
N=5
start=0
total=1
visited=[0]*N
visited[0]=1
stack=[]

def hamiltonian(vertex):
    global total
    global stack
    global start
    global N
    
    if total==N:
        if visited[start]==1:
            
            return True
        return False
    for i in range(N):
        if graph[vertex][i]==1 and visited[i]==0:
            stack.append(i)
            total+=1
            visited[i]=1
            if hamiltonian(i):
                return True
            stack.pop()
            total-=1
            visited[i]=0
    return False

hamiltonian(0)
print(stack)
