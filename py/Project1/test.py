import sys

sys.stdin = open('input.txt', 'r')
# x=list(map(int,input().split()))
# print(type(x))
# print(x)
# print(type(x[0]))
l=list(input().split())
marks_count=int(input())
marks=list(map(int,input().split()))
print(l[0])
def main(l):
    print('Name:',l[0],l[1])
    print('ID:',l[2])
    avg_mark=sum(marks)/marks_count
    print('Grade:', int(avg_mark))

main(l)
