info = []
for i in range(5):
    name, height, weight = input().split()
    info.append({'name':name, 'height':int(height), 'weight':float(weight)})

info.sort(key=lambda x : x['name'])
print('name')
for i in info:
    print(i['name'], i['height'], i['weight'])

info.sort(key=lambda x : -x['height'])
print('\nheight')
for i in info:
    print(i['name'], i['height'], i['weight'])