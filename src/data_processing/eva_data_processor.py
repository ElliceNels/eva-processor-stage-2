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
        self.countries = {record[2] for record in self.records}

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

            records.append((date, duration_hours, country.lower()))

        records.sort(key=lambda record: record[0])
        return records

    def _calculate_cumulative_hours(self):
        for date, duration_hours, country in self.records:
            self.total_hours += duration_hours
            self.dates.append(date)
            self.cumulative_hours.append(self.total_hours)
            self.total_hours_by_country[country] += duration_hours


    def compare_countries(self, country_a, country_b, start_year, end_year):
        if start_year > end_year:
            raise ValueError("Invalid year range")

        if country_a not in self.countries or country_b not in self.countries:
            raise ValueError("Unknown country")

        a_records = self.get_country_records(country_a)
        b_records = self.get_country_records(country_b)

        a_records = self.get_records_in_range(a_records, start_year, end_year)
        b_records = self.get_records_in_range(b_records, start_year, end_year)

        a_stats = self.get_records_stats(a_records)
        b_stats = self.get_records_stats(b_records)

        if a_stats["total"] > b_stats["total"]:
            winner = country_a
        elif b_stats["total"] > a_stats["total"]:
            winner = country_b
        else:
            winner = "Tie"

        return a_stats, b_stats, winner

    def get_country_records(self, country):
        records = []
        for record in self.records:
            if record[2].strip().lower() == country.strip().lower():
                records.append(record)

        return records

    @staticmethod
    def get_records_stats(records):
        count = len(records)
        total = sum(record[1] for record in records)
        average = total / count if count > 0 else None

        return {
            "count": count,
            "total": total,
            "average": average
        }

    @staticmethod
    def get_records_in_range(records, start_year, end_year):
        if start_year > end_year:
            raise ValueError("Start year cannot be after end year")

        filtered_records = []

        for record in records:
            if start_year <= record[0].year <= end_year:
                filtered_records.append(record)

        return filtered_records


    @staticmethod
    def _duration_text_to_hours(duration_text):
        hours, minutes = map(int, duration_text.split(":"))
        return hours + minutes / 60

    def get_countries(self):
        return self.countries

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
