import Date
import pytest

date1 = Date.Date(15,45,21,12,1980)

#properties test
assert date1.hour == 15
assert date1.minute == 45
assert date1.day == 21
assert date1.month == 12
assert date1.year == 1980

#setters test
date1.hour = 5
date1.minute = 40
date1.day = 11
date1.month = 7
date1.year = 2018

assert date1.hour == 5
assert date1.minute == 40
assert date1.day == 11
assert date1.month == 7
assert date1.year == 2018

#invalid data test
with pytest.raises(ValueError):
    date1.hour = 24
with pytest.raises(ValueError):
    date1.hour = -1
with pytest.raises(ValueError):
    date1.minute = 60
with pytest.raises(ValueError):
    date1.minute = -1
with pytest.raises(ValueError):
    date1.day = 0
with pytest.raises(ValueError):
    date1.day = 32
with pytest.raises(ValueError):
    date1.month = 0
with pytest.raises(ValueError):
    date1.month = 13
date1.month = 4
with pytest.raises(ValueError):
    date1.day = 31
date1.month = 2
date1.year = 2000
with pytest.raises(ValueError):
    date1.day = 30
with pytest.raises(ValueError):
    date1 = Date.Date(24,2,30,12,1700)
with pytest.raises(ValueError):
    date1 = Date.Date(12,60,30,12,2000)
with pytest.raises(ValueError):
    date1 = Date.Date(12,2,31,11,2000)
with pytest.raises(ValueError):
    date1 = Date.Date(12,2,30,13,2000)
date2 = Date.Date(5,1,20,2,1700)
with pytest.raises(ValueError):
    date2.day = 29

# overrided methods test
date1 = Date.Date(15,45,21,12,1980)
date2 = Date.Date(15, 8, 21, 12, 1980)
assert date1 == date2
date2.year = 2010
with pytest.raises(AssertionError):
    assert date1 == date2