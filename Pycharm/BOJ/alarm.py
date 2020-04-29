a = input().split(" ")
h = int(a[0])  #시간
m = int(a[1])  #분

if m-45 < 0:
    h = h-1
    if h < 0:
        h = 23
    m = m + 60 - 45
else:
    m = m - 45

print(h, m)