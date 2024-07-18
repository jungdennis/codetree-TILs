a, b, c, d = map(int, input().split())

time_start = 60 * a + b
time_end = 60 * c + d

print(time_end - time_start)