import Main
import pytest

#methods test
#format hmm or hhmm
assert 0 == Main.read_minute('1000')
assert 1 == Main.read_minute('1001')
assert 10 == Main.read_minute('1010')
assert 99 == Main.read_minute('1099')
assert 0 == Main.read_minute('45')
assert 0 == Main.read_minute('10045')

assert 1 == Main.read_hour('150')
assert 10 == Main.read_hour('1005')
assert 99 == Main.read_hour('9910')
assert 0 == Main.read_hour('45')
assert 0 == Main.read_hour('10045')



