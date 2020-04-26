#모듈(module): 미리 작성된 함수 코드를 모아 놓은 파이썬 파일

import keyword  #제공해주는 라이브러리 사용 가능

#math: 다양한 수학적 연산 해주는 라이브러리
import math
print(math.pow(3, 8))  #3의 8제곱 수행
print(math.sqrt(64))  #제곱근 함수
print(math.gcd(72, 24))  #최대공약수 구함

import lib

print(lib.add(3, 7))

from lib import add  #라이브러리 파일이 너무 클 경우, 그 안에 특정한 함수만 불러서 사용 가능

print(add(3, 7))

import lib as t  #라이브러리 파일 이름이 길 경우

print(t.add(3, 7))