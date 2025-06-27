def check_letters(s: str):
    s = s.lower()
    noliki = []

    for i in range(26):
        target = chr(ord("a") + i)
        if target in s:
            noliki.append(1)
        else:
            noliki.append(0)
    l = ''.join([str(i) for i in noliki])
    return l


sssr = chr(int("262D", 16))

print(check_letters('ABcd'))
print(sssr)
print(check_letters('A-Z'))
print(sssr)
print(check_letters('b*e*e*g*e*e*k'))
print(sssr)
print(check_letters('a'))
print(sssr)
print(check_letters('Привет!'))
print(sssr)
print(check_letters('abcdefghijklmnopqrstuvwxyz'))
