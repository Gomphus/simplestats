def mean(vals):
	total = float(sum(vals))
	length = len(vals)
	return total/length

def std(vals):
	if len(vals) == 0:
		return 0.0
	return vals[-1]/2.0


#print mean([2,4])
