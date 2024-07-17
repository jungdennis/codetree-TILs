n = int(input())
student = []

for i in range(n):
    h, w = map(int, input().split())
    student.append({'h':h, 'w':w, 'n':i+1})

student.sort(key=lambda x : (-x['h'], -x['w'], x['n']))

for s in student:
    print(s['h'], s['w'], s['n'])