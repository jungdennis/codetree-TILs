dayofweek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

start_date = 0
for i in range(1, m1):
    start_date += day[i]
start_date += d1

end_date = 0
for i in range(1, m2):
    end_date += day[i]
end_date += d2

print(dayofweek[(end_date - start_date) % 7])