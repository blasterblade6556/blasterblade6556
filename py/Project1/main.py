import sys

sys.stdin = open('input.txt', 'r')
matrix=[]


for i in range(6):
    l = list(map(int, input().rstrip().split()))
    print(l)
    matrix.append(l)

for a in matrix:
    print(a, end="  ")

print(matrix)
