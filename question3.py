from collections import deque
def min_of_max_in_subarrays(k, brightness):
    n = len(brightness)
    max_in_subarrays = []
    dq = deque()
    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and brightness[dq[-1]] <= brightness[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            max_in_subarrays.append(brightness[dq[0]])
    return min(max_in_subarrays)
k = int(input().strip())
n = int(input().strip())
brightness = [int(input().strip()) for _ in range(n)]
result = min_of_max_in_subarrays(k, brightness)
print(result)