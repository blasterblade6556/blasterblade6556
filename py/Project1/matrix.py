import sys

sys.stdin = open('input.txt', 'r')
matrix=[]

w, h = 6, 6;
matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(h):
    l = list(map(int, input().rstrip().split()))
    j=0
    for num in l:
        matrix[i][j]=num
        j+=1
for i in matrix:
    #print(i)

l=[]
for i in range(w-2):
    for j in range(w-2):
        #print(matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+1]+matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2])
        result=matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+1]+matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2]
        l.append(result)
print(max(l))
