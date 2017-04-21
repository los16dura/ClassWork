A = input()
B = input()
C = A + "#" + B
z = [0]*len(C)
left = right = 0
for i in range(0,len(C)):
    x = min(z[i-left],right-i+1) if i <=right else 0
    while i+x < len(C) and C[x] == C[i+x]:
        x+=1
    if i+x-1>right:
        left,right = i,i+x-1
    z[i] = x
s = []
for j in range(len(z)):
    if z[j] == len(A):
        s.append(j-len(A)-1)
if len(s) == 0:
    s.append(-1)
print(*s)
