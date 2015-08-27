
from stats import mean
from nose.tools import assert_equal

def mean(vals):
	total = sum(vals)
	length = len(vals)
	return total/length
def test_mean():
	assert_equal(mean([2,4]), 3)
#test_mean()

def test_float_mean():
	assert_equal(mean([1,2]), 1.5)
#test_float_mean()

def test_newmean():
	assert_equal(test_newmean(-2,2), 0)
#test_newmean()