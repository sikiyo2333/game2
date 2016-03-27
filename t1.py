
from time import ctime,sleep


def timefun_arg(pre ="hello"):
	def timefun(func):
		def wrappedfunc():
			print "%s called at %s %s"%(func.__name__,ctime(),pre)
			return func()
		return wrappedfunc
	return timefun


@timefun_arg("itcast")
def foo():
	print "this is itcast"

@timefun_arg()
def foo():
	print "this is ...."


foo()
sleep(1)
foo()
