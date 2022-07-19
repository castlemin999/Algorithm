'''
a = input("숫자를 입력하세요 : ")
print(a)



# 입력한 값에서 띄어쓰기로 문자를 자른다.
a, b = input("숫자를 입력하세요 : ").split()
print(a+b)

# 숫자형으로 변환
a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(type(a))
print(type(b))
print(a+b)


# map 함수 사용
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(type(a))
print(type(b))
print(a+b)


# 연산자
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #몫
print(a%b)  #나머지
print(a**b) #거듭제곱


'''

a = 4.3
b = 5
c = a + b
print(type(c)) # 실수는 정수를 포함 (더 큰 범위의 데이터 타입으로 결정)
print(c)










