def make_palindrome(n):
    def reverse_number(num):
        result = 0
        while num > 0:
            result = result * 10 + num % 10
            num //= 10
        return result

    def is_palindrome(num):
        if num == reverse_number(num):
            return True
        return False

    if is_palindrome(n):
        return n
    else:
        for i in range(5):
            n += reverse_number(n)
            if is_palindrome(n):
                return n
        return -1


print(make_palindrome(101))
print(make_palindrome(23))
print(make_palindrome(196))
print(make_palindrome(1))
print(make_palindrome(166))
print(make_palindrome(69))
