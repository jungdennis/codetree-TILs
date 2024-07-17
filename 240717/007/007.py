class agent:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

code, point, time = input().split()
secret_agent = agent(code, point, time)

print(f"secret code : {secret_agent.secret_code}")
print(f"meeting point : {secret_agent.meeting_point}")
print(f"time : {secret_agent.time}")