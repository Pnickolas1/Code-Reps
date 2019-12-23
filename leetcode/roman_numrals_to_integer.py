
class Solution:

    def romanToInt(self, s):
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i + 1]] > roman_to_int[s[i]]:
                ans -= roman_to_int[s[i]]
            else:
                ans = ans + roman_to_int[s[i]]
        return ans


x = Solution()
test = x.romanToInt('IV')




def roman_to_ints(roman):
    romanDict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    results = 0
    for i in range(len(roman) - 1, -1, -1):
        if i - 1 >= 0 and romanDict[roman[i]] > romanDict[roman[i -1 ]]:
            results -= romanDict[roman[i]]
        else:
            results += romanDict[roman[i]]
    return results


print(roman_to_ints('XXII'))