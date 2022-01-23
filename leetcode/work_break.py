 

"""
 leetcode 

139 word break

dynamic programming
 
"""


def wordBreak(s, wordDict):

    dp = [False for x in range(len(s) + 1)]
    dp[len(s)] = True

    for i in range(len(s) -1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break
    print(dp)
    return dp[0]

print(wordBreak('neetcode',['neet', 'leet', 'code']))

