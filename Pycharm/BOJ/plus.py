while True:  #무한루프
    try:
        a = input().split(" ")
#        a = a.split(" ")  #x, y = input().split(" ") 가능! -> 한번에 넣을 수 있음.
        print(int(a[0]) + int(a[1]))
    except:  #예외 처리에서 무한루프 탈출
        break