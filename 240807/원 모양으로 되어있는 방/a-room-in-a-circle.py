import sys
n = int(input())

target = []
for i in range(n):
    target.append(int(input()))

min_distance = sys.maxsize
for i in range(n):
    target_move = target[i:] + target[:i]
    # print(target_move) 

    distance = 0
    for j in range(n):
        distance += (j * target_move[j])
    min_distance = min(min_distance, distance)

print(min_distance)