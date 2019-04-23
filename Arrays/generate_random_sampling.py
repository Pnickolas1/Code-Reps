import random


def random_sampling(k, arr):

    for i in range(k):
        # generate a random index in [i, len(arr) -1]
        r = random.randint(i, len(arr) - 1)
        arr[i], arr[r] = arr[r], arr[i]
    return arr

def random_sampling_2(k, A):

    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A


print(random_sampling(2, [3, 7, 5, 11]))

print(random_sampling_2(2, [3, 7, 5, 11]))
