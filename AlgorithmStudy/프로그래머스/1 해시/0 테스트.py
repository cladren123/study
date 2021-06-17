


test = {'kakao' : 2000, 'daeshin' : 3000}

# 딕셔너리 추가
test['naver'] = 8000
print(test)

# 딕셔너리 삭제
del test['daeshin']
print(test)

# 딕셔너리 값 수정
test['kakao'] = 3500
print(test)

# key의 갯수를 나타낸다.
print(len(test))

# key의 목록을 나타낸다.
print(test.keys())

# value의 목록을 나타낸다
print(test.values())

# key, value를 동시에 표시한다.
print(test.items())

# 모든 것 제거
# test.clear()

# 딕셔너리 복사
test1 = test.copy()
print(test1)

# key에 할당된 값 반환
print(test.get('kakao'))

# 기존 딕셔너리에 새로운 딕셔너리 추가
test.update(test1)
print(test)