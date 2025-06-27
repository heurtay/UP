def hamming_distance(s1: str, s2: str):
    counter = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            counter += 1
    return counter


print(hamming_distance('abbcace', 'abacacc'))
print(hamming_distance('beegeek', 'beegeek'))
print(hamming_distance('abcd', 'efgh'))