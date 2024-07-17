class bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

code, color, time = input().split()
b_ = bomb(code, color, time)

print(f"code : {b_.code}")
print(f"color : {b_.color}")
print(f"second : {b_.time}")