
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

print(test)