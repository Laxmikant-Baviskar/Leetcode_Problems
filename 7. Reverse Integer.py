def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    result = 0
    while x != 0:
        digit = x % 10
        x = x // 10
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return 0
        elif result < INT_MIN // 10 or (result == INT_MIN // 10 and digit < INT_MIN % 10):
            return 0
        else:
            result = result * 10 + digit
    return result
