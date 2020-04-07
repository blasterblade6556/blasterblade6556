import sys

sys.stdin = open('input.txt', 'r')
matrix=[]


for i in range(6):
    l = list(map(int, input().rstrip().split()))
    print(l)
    matrix.append(l)
print(matrix)

for i in matrix:
    print(i)
    print()
    for j in i:
        print(i)
        print(j)
        print()
