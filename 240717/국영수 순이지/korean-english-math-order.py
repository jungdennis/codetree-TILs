n = int(input())
score = []

for i in range(n):
    name, kor, eng, math = input().split()
    score.append({'name':name, 'kor':int(kor), 'eng':int(eng), 'math':int(math)})

score.sort(key=lambda x : (-x['kor'], -x['eng'], -x['math']))

for s in score:
    print(s['name'], s['kor'], s['eng'], s['math'])