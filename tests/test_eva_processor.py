
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_processing.eva_data_processor import EVADataProcessor

def make_processor():
    data = [
        {"date": "2000-01-01", "duration": "02:00", "country": "usa"},
        {"date": "2005-06-01", "duration": "04:00", "country": "usa"},
        {"date": "2010-12-31", "duration": "03:00", "country": "russia"},
        {"date": "2020-01-01", "duration": "01:00", "country": "russia"},
    ]
    return EVADataProcessor(data)

def test_existing_functionality():
    """processor should correctly calculate total hours and cumulative hours based on the provided EVA data."""

    processor = make_processor()

    assert processor.get_total_hours() == 10.0
    assert processor.get_cumulative_hours() == [2.0, 6.0, 9.0, 10.0]

def test_country_comparison_happy():
    """processor should correctly compare two countries and return their EVA statistics and the winner."""

    processor = make_processor()

    usa, russia, winner = processor.compare_countries("usa", "russia", 2000, 2010)

    assert usa["count"] == 2
    assert usa["total"] == 6.0
    assert usa["average"] == 3.0

    assert russia["count"] == 1
    assert russia["total"] == 3.0
    assert russia["average"] == 3.0

    assert winner == "usa"

def test_invalid_year_range():
    """processor should raise a ValueError when the start year is greater than the end year."""

    processor = make_processor()

    try:
        processor.compare_countries("usa", "russia", 2020, 2000)
    except ValueError:
        return
    assert False, "Expected ValueError for invalid year range"


def test_no_matching_evas():
    """processor should return zero statistics and a tie when there are no matching EVAs for the given countries and year range."""
    processor = make_processor()

    usa, russia, winner = processor.compare_countries("usa", "russia", 1990, 1995)

    assert usa == {"count": 0, "total": 0, "average": None}
    assert russia == {"count": 0, "total": 0, "average": None}
    assert winner == "Tie"


def test_unknown_country():
    """processor should raise a ValueError when one or both of the countries are not present in the EVA data."""
    processor = make_processor()

    try:
        processor.compare_countries("mars", "usa", 2000, 2010)
    except ValueError:
        return

    assert False, "Expected ValueError for unknown country"


if __name__ == "__main__":
    test_existing_functionality()

    test_country_comparison_happy()
    test_invalid_year_range()
    test_no_matching_evas()
    test_unknown_country()

    print("All 5 tests passed!")
