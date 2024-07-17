class agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

min_score = 999
min_idx = 9
agents = []
for i in range(5):
    name, score = input().split()
    score = int(score)
    agents.append(agent(name, score))

    if score < min_score:
        min_score = score
        min_idx = i

min_agent = agents[min_idx]
print(f"{min_agent.name} {min_agent.score}")