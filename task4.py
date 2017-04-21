first = input()
second = input()
C = second+"#"+first+first
z = [0]*len(C)
left = right = 0
for i in range(1,len(C)):
    x = min(z[i-left],right-i+1) if i <=right else 0
    while i+x < len(C) and C[x] == C[i+x]:
        x+=1
    if i+x-1>right:
        left,right = i,i+x-1
    z[i] = x
for j in range(len(first)+1,len(C)):
    if z[j] >= len(first):
        d = j - (len(first)+1)
        break
    else:
        d = -1
print(d)
print(z)