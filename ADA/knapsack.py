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
    
    def dynamic(self):
        dp=[[0]*(self.target+1)]*(self.N+2)
        
        for i in range(self.N+1,-1,-1):
            for j in range(self.target+1):
                if i==self.N+1 or j==0:
                    dp[i][j]=0
                elif j < self.weights[i]:
                    dp[i][j]=dp[i+1][j]

                else:
                   dp[i][j]=max(dp[i+1][j-self.weights[i]]+self.values[i],dp[i+1][j])
        print( dp[0][self.target])




k= Knapsack(1,[10,20],[60,120],15)
k.dynamic()
print(k.solve(0,-1))
