s1 = list(input())
a = [0]*len(s1)
j = 0
x = 0
i = 1
while i < len(s1)+1:
    while i+j<len(s1) and s1[i+j] == s1[j]:
        j+=1
        if a[j+i-1]<j:
            a[j+i-1]=j
    i+=1
    j = 0
print(*a)
