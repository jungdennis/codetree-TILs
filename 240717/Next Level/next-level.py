class user:
    def __init__(self, id, level):
        self.id = id
        self.level = level

user1 = user('codetree', 10)
id, level = input().split()
level = int(level)
user2 = user(id, level)

for u in [user1, user2]:
    print(f"user {u.id} lv {u.level}")