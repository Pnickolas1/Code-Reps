


def intToRoman(num):
    d = {
        1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL',
         10: 'X',
         9: 'IX',
         5: 'V',
         4: 'IV',
         1: 'I'
    }
    res = ''
    for k in d:
        while num >= k:
            print(num, k)
            res += d[k]
            num -= k
    return res

print(intToRoman(45))


def ints_To_roman(number):
    d = {
        1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL',
         10: 'X',
         9: 'IX',
         5: 'V',
         4: 'IV',
         1: 'I'
    }
    result = ""
    for k in d:
        if k <= number:
            result += d[k]
            number -= k
    return result

print(ints_To_roman(120))
