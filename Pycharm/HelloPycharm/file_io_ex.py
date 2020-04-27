def process(filename):
    with open(filename, "r") as f:
        #키: 알파벳, 값: 빈도수
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

dict = process("input_eng.txt")
#print(dict)

#빈도수를 기준으로 내림차순으로 정렬을 수행
dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)
#정렬기준은 값이 되도록 -> 한쌍인 a를 확인할껀데 그 중 value인 a[1]을 기준으로
#print(dict)
for data, count in dict: #튜플 형태
    if data == '\n' or data == ' ':
        continue
    print("%d번 출현: [%c]" %(count, data))