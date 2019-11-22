class Knapsack:
    def __init__(self,N,weights,values,target):
        self.weights=weights
        self.values=values
        self.N=N 
        self.target=target 
        

    
    def solve(self,W, i):
        if i==self.N: 
            return 0
        """if i==-1:
            return max(self.solve(W+self.weights[i+1],i+1), self.solve(W,i+1))"""
        if W+self.weights[i+1] > self.target :
            return self.solve(W,i+1)
        
        

        return max(self.values[i+1]+self.solve(W+self.weights[i+1],i+1), self.solve(W,i+1))
    
k= Knapsack(1,[10,4],[60,12],5)
print(k.solve(0,-1))
