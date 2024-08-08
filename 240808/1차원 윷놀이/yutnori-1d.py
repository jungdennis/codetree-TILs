n, m, k = map(int, input().split())
delta = list(map(int, input().split()))
order = []
max_score = 0

def pick(x):
    if x >= n:
        global max_score
        
        location = [1] * k
        for i in range(len(order)):
            location[order[i]] += delta[i]

        score = 0
        for l in location:
            if l >= m:
                score += 1

        if score > max_score:
            # print(order, location, score)
            max_score = score

        return

    for i in range(k):
        order.append(i)
        pick(x+1)
        order.pop()

pick(0)
print(max_score)