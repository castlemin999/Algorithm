'''
주석 처리
'''
a = 1
A = 2
A1 = 3
#2b = 4
_b = 4

print(a, A, A1, _b)

a, b, c = 3, 2, 1

print (a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)


#변수 타입
a=12345
print(type(a)) #정수 (int)

a = 12.1234556751
print(type(a)) #실수 (float)

a = 'student'
print(type(a)) # 문자열 (string)

#출력방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)


#구분자
print(a, b, c, sep=', ')    
print(a, b, c, sep=',')
print(a, b, c, sep='')
print(a, b, c, sep='\n') #줄바꿈

print(a, end= ' ') #print 자동 줄바꿈을 없애준다.
print(b, end= ' ')
print(c)