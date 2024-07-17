class info:
    def __init__(self, name, post, address):
        self.name = name
        self.post = post
        self.address = address

n = int(input())
max_idx = n
max_name = "aaaaaaaaaa"
infos = []
for i in range(n):
    name, post, address = input().split()
    infos.append(info(name, post, address))

    compare_list = [name, max_name]
    compare_list.sort()

    if compare_list[1] == name:
        max_idx = i
        max_name = name

max_info = infos[max_idx]
print(f"name {max_info.name}")
print(f"addr {max_info.post}")
print(f"city {max_info.address}")