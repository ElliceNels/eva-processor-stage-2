import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

with open("data/eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []

for eva in eva_data:
    date_text = eva.get("date")
    duration_text = eva.get("duration")
    country = eva.get("country")
    if not country:
        country = ""

    if not date_text or not duration_text:
        continue

    date = datetime.fromisoformat(date_text)
    hours, minutes = map(int, duration_text.split(":"))
    duration_hours = hours + minutes / 60

    records.append((date, duration_hours, country))

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0
total_hours_by_country = Counter()

for date, duration_hours, country in records:
    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)
    total_hours_by_country[country] += duration_hours

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot cumulative_hours for all countries
ax1.plot(dates, cumulative_hours)
ax1.set_xlabel("Year")
ax1.set_ylabel("Cumulative EVA duration (hours)")
ax1.set_title("Cumulative EVA Duration")

# Bar chart of each country
countries = list(total_hours_by_country.keys())
hours = list(total_hours_by_country.values())
ax2.bar(countries, hours)
ax2.set_ylabel("Total hours")
ax2.set_title("Total Hours by Country")
ax2.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("out/cumulative_duration.png")
plt.show()
