def dp(n):
    if n==1: return [[1]]
    else:
        Z=[]
        for i in range (1,(n-1)//2+1):
            for j in dp(n-i):
                if i < min(j):
                    Z.append([i]+j)
        return Z+[[n]]  

#Examples
        
for x in dp(11):
    print(f"11  = {'+'.join([str(y) for y in x])}")

print(f"\nThere are {len(dp(11))} distinct partitions of 11")    

for x in dp(30):
    print(f"30  = {'+'.join([str(y) for y in x])}")

print(f"\nThere are {len(dp(30))} distinct partitions of 30")    
