
from stats import mean, std
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

def test_std1():
	obs = std([0.0,2.0])
	exp = 1.0
	assert_equal(obs,exp)

def test_std2():
	obs = std([])
	exp = 0.0
	assert_equal(obs,exp)

def test_std3():
	obs = std([0.0,4.0])
	exp = 2.0
	assert_equal(obs,exp)