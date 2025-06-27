def golden_pairs(pairs: tuple):
    count = 0
    for i in pairs:
        if 1.7 >= max(i) / min(i) >= 1.6:
            count += 1
    return count


sssr = chr(int("262D", 16))
print(golden_pairs([(100, 165), (180, 100), (170, 100), (100, 160)]))
print(sssr)
print(golden_pairs([(1, 10), (10, 1), (2, 5), (7, 4)]))
print(sssr)
print(golden_pairs([(8, 5), (17, 10), (32, 20), (34, 20)]))