m1, d1, m2, d2 = map(int, input().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_day = 0
for i in range(m1):
    start_day += day[i]
start_day += d1

end_day = 0
for i in range(m2):
    end_day += day[i]
end_day += d2


print(end_day - start_day + 1)