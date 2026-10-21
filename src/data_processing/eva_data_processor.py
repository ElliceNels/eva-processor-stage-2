from datetime import datetime
from collections import Counter

class EVADataProcessor:

    def __init__(self, eva_data):
        self.records = self._parse_eva_data(eva_data)
        self.total_hours = 0
        self.total_hours_by_country = Counter()
        self.dates = []
        self.cumulative_hours = []
        self._calculate_cumulative_hours()

    def _parse_eva_data(self, eva_data):
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
            duration_hours = EVADataProcessor._duration_text_to_hours(duration_text)

            records.append((date, duration_hours, country))

        records.sort(key=lambda record: record[0])
        return records

    def _calculate_cumulative_hours(self):
        for date, duration_hours, country in self.records:
            self.total_hours += duration_hours
            self.dates.append(date)
            self.cumulative_hours.append(self.total_hours)
            self.total_hours_by_country[country] += duration_hours

    @staticmethod
    def _duration_text_to_hours(duration_text):
        hours, minutes = map(int, duration_text.split(":"))
        return hours + minutes / 60

    def get_records(self):
        return self.records

    def get_total_hours(self):
        return self.total_hours

    def get_total_hours_by_country(self):
        return self.total_hours_by_country

    def get_dates(self):
        return self.dates

    def get_cumulative_hours(self):
        return self.cumulative_hours
