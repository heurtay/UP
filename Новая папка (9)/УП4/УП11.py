def mystery(n: int):
    counter = 0
    lst = []
    lst.extend(str(n))
    for i in lst:
        if i == '0':
            counter += 1
        elif i == '9':
            counter += 1
        elif i == '8':
            counter += 2
        elif i =='6':
            counter += 1
    return counter


print(mystery(0))
print(mystery(1))
print(mystery(10))
print(mystery(18))
print(mystery(80))
print(mystery(90))
print(mystery(13))
print(mystery(134))
print(mystery(1346))
print(mystery(888))
print(mystery(1000))
print(mystery(2222))
print(mystery(8888))
print(mystery(9999))
print(mystery(10000))