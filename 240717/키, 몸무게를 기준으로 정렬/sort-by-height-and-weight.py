n = int(input())
info = []

for i in range(n):
    name, height, weight = input().split()
    info.append({'name':name, 'height':int(height), 'weight':int(weight)})

info.sort(key=lambda x : (x['height'], -x['weight']))

for i in info:
    print(i['name'], i['height'], i['weight'])