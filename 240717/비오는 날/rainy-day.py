import datetime

class forecast:
    def __init__(self, date, dayofweek, weather):
        self.date = date
        self.dayofweek = dayofweek
        self.weather = weather

n = int(input())
rainy = []

for i in range(n):
    date, dayofweek, weather = input().split()

    if weather == 'Rain':
        rainy.append(forecast(date, dayofweek, weather))

fast_rain = forecast('2100-12-31', "Sun", "Rain")
for rainy_day in rainy:
    fast_year, fast_month, fast_day = map(int, fast_rain.date.split("-"))
    year, month, date = map(int, rainy_day.date.split("-"))

    if year < fast_year:
        fast_rain = rainy_day
    elif year == fast_year:
        if month < fast_month:
            fast_rain = rainy_day
        elif month == fast_month:
            if day < fast_day:
                fast_rain = rainy_day

print(f"{fast_rain.date} {fast_rain.dayofweek} {fast_rain.weather}")