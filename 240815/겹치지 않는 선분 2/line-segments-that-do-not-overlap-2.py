n = int(input())

line = []
for i in range(n):
    x1, x2 = map(int, input().split())
    line.append((x1, x2))

overlapped = [1] * n

def check_overlap(line1, line2):
    x1_1, x1_2 = line1
    x2_1, x2_2 = line2

    x1_min, x1_max = sorted(line1)
    x2_min, x2_max = sorted(line2)

    if max(x1_min, x2_min) > min(x1_max, x2_max):
        return False
    else:
        a1 = 1 / (x1_2 - x1_1)
        a2 = 1 / (x2_2 - x2_1)

        if a1 == a2:
            return False
        else:
            overlap_x = (a2 * x2_1 - a1 * x1_1) / (a2 - a1)
            overlap_y = a1 * a2 * (x2_1 - x1_1) / (a2 - a1)
            if overlap_x >= max(x1_1, x2_1) and overlap_x <= min(x1_2, x2_2) and overlap_y >= 0 and overlap_y <= 1:
                return True
            else:
                return False

for i in range(n):
    for j in range(i+1, n):
        if check_overlap(line[i], line[j]):
            overlapped[i] = 0
            overlapped[j] = 0

print(sum(overlapped))