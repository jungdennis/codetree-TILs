n = int(input())

info = []

for i in range(n):
    name, height, weight = input().split()
    height = int(height)
    weight = int(weight)

    info.append({'name' : name, 'height' : height, 'weight' : weight})

info.sort(key=lambda x : x['height'])

for i in info:
    print(i['name'], i['height'], i['weight'])