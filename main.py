import bisect

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
points = []
toitaka = []
for ind, j in enumerate(S):
    a = [A[ind2] for ind2, k in enumerate(list(j)) if k == "o"]
    points.append(sum(a)+ind+1)
    toitaka.append([i == "o" for i in list(j)])
print(points)
print(toitaka)

now_mx = max(points)
result = []
for ind, j in enumerate(points):
    if now_mx == j:
        result.append(0)
    n = now_mx - j + 1
    nowt = [A[ind2] for ind2, k in enumerate(toitaka[ind]) if not k]
    nowt.sort(reverse=True)
    ct = 0
    score = j
    print(ind, n)
    for i in nowt:
        ct += 1
        score += i
        if score >= n:
            now_mx = score
            break
    print(score)
    result.append(ct)
print(*result)

            
