a, b, c = map(int, input().split())

start_time = 11 * 24 * 60 + 11 * 60 + 11
end_time = a * 24 * 60 + b * 60 + c

if start_time <= end_time:
    print(end_time - start_time)
else:
    print(-1)