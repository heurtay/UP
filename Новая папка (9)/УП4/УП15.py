def longest_substring_without_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_no_vowels = ''
    lst_no_vowels = []
    for i in s:
        if i in vowels:
            lst_no_vowels.append(str_no_vowels)
            str_no_vowels = ''
        else:
            str_no_vowels += i
    lst_no_vowels.append(str_no_vowels)

    return max([len(x) for x in lst_no_vowels])


print(longest_substring_without_vowels('abcdefg'))
print(longest_substring_without_vowels('bcdgf'))
print(longest_substring_without_vowels('aeiou'))
print(longest_substring_without_vowels('abecidofug'))
print(longest_substring_without_vowels('x'))
print(longest_substring_without_vowels('abbbabbaba'))
