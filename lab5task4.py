class Time(object):
	def __init__(caller,t):
		caller.t=t
		caller.mm,caller.ss = divmod(t,60)
		caller.hh,caller.mm= divmod(caller.mm,60)
		
	def print_time(caller):
		print("{:02}:{:02}:{:02}" .format(caller.hh,caller.mm,caller.ss))

	def is_after(caller,other):
		return other.t>caller.t

t1 = Time(360)
t2 = Time(640)
t1.print_time()
print(t1.is_after(t2))
