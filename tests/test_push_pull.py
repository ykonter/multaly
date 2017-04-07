from connector.push_pull import *


def test_data_gen():
    dat = data_gen()
    t = dat['time_stamp']
    assert t.day == dat['day']
    assert t.year == dat['year']
    assert t.month == dat['month']