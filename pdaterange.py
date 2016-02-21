#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

"""
Recieve an input string and output a range of dates based on that

The string should be in some format like
"from 4 feb to 8 feb 2016"

But I want to build it farily smart to be able to handle various text inputs
"""


from datetime import datetime, timedelta
import sys
import re
import itertools


class PrintDateRange:
    """
    Print a date range from a start date to an end date
    """
    def __init__(self, date_string):
        self.date_string = date_string

    def tokenize(self):
        """
        Take the date_string and interpret it as a list

        Returns a list if given a string, otherwise returns False
        """
        try:
            return re.split(" |\/|-", self.date_string)
        except TypeError:
            return False

    def _chopdates(self, li):
        """
        chop out unwanted strings from datelist
        """
        return [x for x in itertools.dropwhile(lambda x:not x.isdigit(), li)]

    def remove_strings(self):
        """
        Take the tokenized list and take off leading
        strings, and intermediate strings

        Does do error checking just to make sure that
        in the end the list has six tokens passed back.
        """
        dates_set = self.tokenize()
        if not dates_set:
            return False
        if len(dates_set) > 6:
            dates_set = self._chopdates(dates_set)
        if len(dates_set) > 6:
            dates_set = dates_set[:3] + self._chopdates(dates_set[3:])
        if len(dates_set) is not 6:
            dates_set = False
        return dates_set

    def interpret_date_string(self):
        """
        Interpret an input string to extract start date
        and end date

        """
        breakup_string = self.remove_strings()
        if not breakup_string:
            return False

        start_date_args = tuple(breakup_string[:3])
        end_date_args = tuple(breakup_string[3:])

        start_date = self.format_date(start_date_args)
        end_date = self.format_date(end_date_args)

        if start_date and end_date:
            return [start_date, end_date]
        else:
            return False

    def make_date_range(self):
        dates = self.interpret_date_string()
        if not dates:
            return False
        iter_date, end_date = dates

        if iter_date >= end_date:

            raise NameError("Bad Date Order")
        add_day = timedelta(days=1)
        date_range = []
        while iter_date <= end_date:
            date_range.append("{:%d %b}".format(iter_date))
            iter_date += add_day
        return date_range

    def format_date(self, args_tup):
        try:
            return datetime.strptime("{0} {1} {2}".format(*args_tup), "%d %b %Y")
        except ValueError:
            pass
        try:
            return datetime.strptime("{0} {1} {2}".format(*args_tup), "%d %B %Y")
        except ValueError:
            pass
        try:
            return datetime.strptime("{0} {1} {2}".format(*args_tup), "%d %m %Y")
        except:
            pass
        return False


if __name__ == "__main__":
    arg_string = " ".join(sys.argv[1:])
    daterangeobj = PrintDateRange(arg_string)
    date_range = daterangeobj.make_date_range()
    for adate in date_range:
        print(adate)
