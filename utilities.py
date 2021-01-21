from datetime import datetime

class Utilities:

    @staticmethod
    def add_year_to_current_date(old_date):
        # This will take a given month and day date format and add the current year to it.
        # old_date - Currently this only handles either Month and Day without slashes or comma's. Month can be digit, 3 letter month or fully spelled.
        return f"{old_date} {datetime.today().year}"

    @staticmethod
    def convert_date_format(date_to_convert):
        # Convert date format that is Month and Day to Month, Day, Year.
        # date_to_convert - The date format that needs to be used currently is a 3 leter month with day, and year. No comma's or slashes.
        try:
            return datetime.strptime(date_to_convert, '%b %d %Y').date().isoformat()
        except ValueError:
            return datetime.today().date().isoformat()
