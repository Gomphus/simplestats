
from stats import mean
from nose.tools import assert_equal

def mean(vals):
	total = sum(vals)
	length = len(vals)
	return total/length
def test_mean():
	assert_equal(mean([2.0,4.0]), 3)
#test_mean()

def test_float_mean():
	assert_equal(mean([1.0,2.0]), 1.5)
#test_float_mean()

def test_newmean():
	assert_equal(mean([-2.0,2.0]), 0)
	return mean
print mean
#test_newmean()