try:     #어떤 내용 실행
    print(3 / 0)
except:  #오류 발생시 실행
    print("0으로는 나눌 수 없습니다.")
else:    #오류가 발생하지 않으면 실행
    print("예외 없이 성공적으로 실행되었습니다.")
finally: #오류에 상관없이 실행
    print("예외 처리를 마칩니다.")

try:
    print(3 / 0)
except Exception as e:  #오류메세지를 e에 넣음
    print(e)