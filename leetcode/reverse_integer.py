




def reverse_integer(number):
    result, remaining = 0, abs(number)
    while remaining:
        result = result * 10 + remaining % 10
        remaining //= 10
    return (result * -1) if number < 0 else result

