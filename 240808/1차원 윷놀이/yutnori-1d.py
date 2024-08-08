n, m, k = map(int, input().split())
delta = list(map(int, input().split()))
location = [1] * k
max_score = 0

def pick(x):
    if x >= n:
        global max_score
        
        score = 0
        for l in location:
            if l >= m:
                score += 1

        if score > max_score:
            # print(order, location, score)
            max_score = score

        return

    for i in range(k):
        if location[i] >= m:
            continue

        location[i] += delta[x]
        pick(x+1)
        location[i] -= delta[x]

pick(0)
print(max_score)