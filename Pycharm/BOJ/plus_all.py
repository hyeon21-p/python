import sys

i = int(input())
#my_function = lambda x, y: x + y

for j in range(0, i):
    num = sys.stdin.readline()  #input()과 같은 기능. But! 속도 면에서 더 빠름.
    num = num.rstrip('/n').split(" ")
    x = int(num[0])
    y = int(num[1])
    print(x + y)

#sum = list(map(my_function, x, y))
#print(sum)
