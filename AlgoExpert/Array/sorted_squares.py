
nums = [-10, -8, -3, -2, 4, 5, 6, 50]


def sortedSquares(array):

    negs = []
    pos = []
    ans = []

    for num in array:
        if num < 0:
            negs.append(num**2)
        else:
            pos.append(num**2)
    print(negs, pos)
    np = len(negs) - 1
    pp = 0

    while np >= 0 and pp < len(pos):
        if negs[np] < pos[pp]:
            ans.append(negs[np])
            np -= 1
        else:
            ans.append(pos[pp])
            pp += 1

    while pp < len(pos):
        ans.append(pos[pp])
        pp += 1

    while np >= 0:
        ans.append(negs[np])
        np -= 1


    return ans



print(sortedSquares(nums))
