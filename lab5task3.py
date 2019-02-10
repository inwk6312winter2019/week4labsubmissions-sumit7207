class Time(object):
	def __init__(caller,hh,mm,ss):
		caller.hh = hh
		caller.mm = mm
		caller.ss = ss
	def print_time(caller):
		print("{:02}:{:02}:{:02}" .format(caller.hh,caller.mm,caller.ss))

t1 = Time(18,46,7)
t1.print_time()
