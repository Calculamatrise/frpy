from math import floor

def t2t(ticks):
	t = int(float(ticks) / 30 * 1e3)
	e = floor(t / 6e4)
	return str(e).zfill(2) + ':' + str(round((t - 6e4 * e) / 1e3, 2)).zfill(5)