def count_treasures(s, queries):
    prefix_sum = [0] * (len(s) + 1)
    
    for i in range(1, len(s) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (1 if s[i - 1] == 'T' else 0)

    results = []
    for start, end in queries:
        results.append(prefix_sum[end] - prefix_sum[start - 1])

    return results

s = input().strip()
n = int(input().strip())
queries = [tuple(map(int, input().strip().split())) for _ in range(n)]

results = count_treasures(s, queries)
for result in results:
    print(result)