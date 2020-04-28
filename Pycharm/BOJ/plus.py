while True:  #무한루프
    try:
        a = input()
        a = a.split(" ")
        print(int(a[0]) + int(a[1]))
    except:  #예외 처리에서 무한루프 탈출
        break