import pytest
from ..utilities import Utilities
from datetime import datetime


def test_date_with_year():
    assert Utilities.add_year_to_current_date("Jan 10") == f"Jan 10 {datetime.today().year}"

def test_error_gives_current_day():
    assert Utilities.convert_date_format("28m") == datetime.today().date().isoformat()
