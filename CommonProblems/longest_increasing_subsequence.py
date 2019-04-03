
# dynamic programming

random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]


def longest_increasing_subsequence(sequence):
    P = [0] * len(sequence)
    M = [0] * (len(sequence) + 1)
    L = 0

    for i in range(len(sequence)):
        lo = 1
        hi = L

        while lo <= hi:
            mid = int((lo + hi) / 2)
            if sequence[M[mid]] < sequence[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo

        P[i] = M[newL - 1]
        M[newL] = i

        L = max(L, newL)

    S = [0] * L
    k = M[L]

    for i in range(L - 1, -1, -1):
        S[i] = sequence[k]
        k = P[k]

    return S


if __name__ == "__main__":
    print(longest_increasing_subsequence(random_numbers))