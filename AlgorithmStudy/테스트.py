
gibondict = dict()

gibondict['a'] = 10
gibondict['b'] = 20
gibondict['c'] = [10]

print(gibondict)

# key 안의 값을 출력
check = gibondict.get('c')
print(check)

# value 리스트의 값 추가
gibondict.get('c').append(200)
print(gibondict)

gibondict['a'] = max(30, gibondict.get('a'))
print(gibondict)

gibondict['a'] = max(20, gibondict.get('a'))
print(gibondict)

gibondict['a'] = max(40, gibondict.get('a'))
print(gibondict)

if 'e' in gibondict :
    gibondict['e'] = max(40, gibondict.get('e'))
else :
    gibondict['e'] = 30
print(gibondict)


if 'e' in gibondict :
    gibondict['e'] = max(40, gibondict.get('e'))
else :
    gibondict['e'] = 30
print(gibondict)


