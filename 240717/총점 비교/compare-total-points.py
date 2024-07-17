n = int(input())
score = []
for i in range(n):
    name, s1, s2, s3 = input().split()
    score.append({'name':name, 's1':int(s1), 's2':int(s2), 's3':int(s3)})

score.sort(key=lambda x : x['s1'] + x['s2'] + x['s3'])

for s in score:
    print(s['name'], s['s1'], s['s2'], s['s3'])