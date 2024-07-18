def count_day(m, d):
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_count = 0
    for i in range(1, m):
        day_count += day[i]
    day_count += d

    return day_count

dayofweek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
A = dayofweek.index(input())

start_day = count_day(m1, d1)
end_day = count_day(m2, d2)

if A <= ((end_day - start_day) % 7):
    print((end_day - start_day) // 7 + 1)
else:
    print((end_day - start_day) // 7)