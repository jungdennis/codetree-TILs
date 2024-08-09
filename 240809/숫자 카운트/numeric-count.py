nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

n = int(input())
guess = []
for i in range(n):
    num, strike, ball = input().split()
    strike = int(strike)
    ball = int(ball)

    guess.append((num, strike, ball))

def baseball(p, g):
    s = 0
    b = 0

    for i in range(3):
        if p[i] == g[i]:
            s += 1
        elif p[i] in g:
            b += 1
    
    return s, b

cnt = 0
for i in range(9):
    for j in range(9):
        for k in range(9):
            if i != j and j != k and k != i:
                possible = nums[i] + nums[j] + nums[k]
                flag = True

                for num_, strike, ball in guess:
                    s, b = baseball(possible, num_)
                    # print(possible, num_, s, b)

                    if s != strike or b != ball:
                        flag = False
                        break

                if flag:
                    cnt += 1

print(cnt)