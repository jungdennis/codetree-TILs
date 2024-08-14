n = int(input())

point = []
for i in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

def triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    if x1 == x2 and (y2 == y3 or y1 == y3):
        dy = abs(y1 - y2)
        
        if y2 == y3:
            dx = abs(x2 - x3)
        elif y1 == y3:
            dx = abs(x1 - x3)

        return dx * dy

    if x2 == x3 and (y1 == y2 or y1 == y3):
        dy = abs(y2 - y3)
        
        if y1 == y2:
            dx = abs(x1 - x2)
        elif y1 == y3:
            dx = abs(x1 - x3)

        return dx * dy
    
    if x1 == x3 and (y1 == y2 or y2 == y3):
        dy = abs(y1 - y3)
        
        if y1 == y2:
            dx = abs(x1 - x2)
        elif y2 == y3:
            dx = abs(x2 - x3)

        return dx * dy

    return 0

max_pad = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            p1, p2, p3 = point[i], point[j], point[k]

            pad = triangle(p1, p2, p3)
            max_pad = max(pad, max_pad)

print(max_pad)