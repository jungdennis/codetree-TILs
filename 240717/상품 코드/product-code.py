class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

product1 = product('codetree', '50')

name, code = input().split()
product2 = product(name, code)

for p in [product1, product2]:
    print(f"product {p.code} is {p.name}")