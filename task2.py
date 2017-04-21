s = input()
z = [0]*len(s)
left = right = 0
for i in range(1,len(s)):
    x = min(z[i-left],right-i+1) if i <=right else 0
    while i+x < len(s) and s[x] == s[i+x]:
        x+=1
    if i+x-1>right:
        left,right = i,i+x-1
    z[i] = x
print(*z)

