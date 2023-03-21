from datetime import datetime

class Utilities:

    @staticmethod
    def add_year_to_current_date(old_date):
        # This will take a given month and day date format and add the current year to it.
        # old_date - Currently this only handles either Month and Day without slashes or comma's. Month can be digit, 3 letter month or fully spelled.
        return f"{old_date} {datetime.today().year}"

    @staticmethod
    def convert_date_format(date_to_convert):
        # Converts the date format string from "2023-03-17T13:10:00-04:00" by splitting out the time stamp and just using year month date.
        date_time_array = date_to_convert.split("T")
        try:
            return datetime.strptime(date_time_array[0], '%Y-%m-%d').date().isoformat()
        except ValueError as e:
            print(f'The following date format is not valid {e}. Returning a default date.')
            return datetime.today().date().isoformat()
