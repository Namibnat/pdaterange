#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

"""
Test module for daterange
"""


import unittest
import datetime
from pdaterange import PrintDateRange


class PrintDateRangeTest(unittest.TestCase):
    def setUp(self):
        self.test1 = "From 2 Feb 2017"
        self.test2 = 45
        self.test3 = "from 2/02/2017 to 27/02/2017"
        self.test4 = "From 2 Feb 2017 to 27 Feb 2017"
        self.test5 = "from 2-02-2017 to 27-02-2017"
        self.test6 = "from 2-02-2017 to 4-02-2017"
        self.test7 = "from 4-02-2017 to 2-02-2017"

    def test_tokenize_s1(self):
        p = PrintDateRange(self.test1)
        tl = p.tokenize()
        assert tl == ["From", "2", "Feb", "2017"]

    def test_tokenize_s2(self):
        p = PrintDateRange(self.test2)
        tl = p.tokenize()
        assert not tl

    def test_tokenize_s3(self):
        p = PrintDateRange(self.test3)
        tl = p.tokenize()
        assert tl == ["from", "2", "02", "2017", "to", "27", "02", "2017"]

    def test_remove_strings_s1(self):
        p = PrintDateRange(self.test4)
        stl = p.remove_strings()
        assert stl == ["2", "Feb", "2017", "27", "Feb", "2017"]

    def test_remove_strings_s2(self):
        p = PrintDateRange(self.test1)
        stl = p.remove_strings()
        assert not stl

    def test_remove_strings_s3(self):
        p = PrintDateRange(self.test2)
        stl = p.remove_strings()
        assert not stl

    def test_interpret_date_string(self):
        p = PrintDateRange(self.test2)
        dtsl = p.interpret_date_string()
        assert not dtsl

    def test_interpret_date_string_s2(self):
        p = PrintDateRange(self.test3)
        dtsl = p.interpret_date_string()
        assert dtsl == [datetime.datetime(2017, 2, 2, 0, 0), datetime.datetime(2017, 2, 27, 0, 0)]

    def test_interpret_date_string_s3(self):
        p = PrintDateRange(self.test4)
        dtsl = p.interpret_date_string()
        assert dtsl == [datetime.datetime(2017, 2, 2, 0, 0), datetime.datetime(2017, 2, 27, 0, 0)]

    def test_interpret_date_string_s4(self):
        p = PrintDateRange(self.test5)
        dtsl = p.interpret_date_string()
        assert dtsl == [datetime.datetime(2017, 2, 2, 0, 0), datetime.datetime(2017, 2, 27, 0, 0)]

    def test_make_date_range_s1(self):
        p = PrintDateRange(self.test6)
        dr = p.make_date_range()
        assert dr == ['02 Feb', '03 Feb', '04 Feb']
