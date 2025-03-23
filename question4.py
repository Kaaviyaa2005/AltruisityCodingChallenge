def min_swaps_to_transform(A, B):
    if sorted(A) != sorted(B):
        return -1
    swaps = 0
    A = list(A)
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] == B[i]:
                for k in range(j, i):
                    A[k], A[k + 1] = A[k + 1], A[k]
                    swaps += 1
                break
    return swaps
n = int(input().strip())
A = input().strip()
B = input().strip()
result = min_swaps_to_transform(A, B)
print(result)