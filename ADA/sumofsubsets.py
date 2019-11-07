set=[]
print("Enter elements")
array= [int(i) for i in input().split(" ")]
print("enter target")
target=int(input())
end=len(array)

def fun(start, sum):
    if sum==target:
        print(set)
        return
    if sum<target:
        for i in range((start+1),end):
            set.append(array[i])
            fun(i, sum+array[i])
            set.pop()
    return
fun(-1,0)
