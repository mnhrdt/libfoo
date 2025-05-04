__foo = 0

def __setup_functions():
	global __foo
	if __foo != 0: return

	from os.path import dirname
	from ctypes import CDLL, POINTER, c_float, c_int

	__foo = CDLL(f"{dirname(__file__)}/libfoo.so").foo
	__foo.argtypes = [POINTER(c_float), c_int]
	__foo.restype = None


def foo(x):
	if isinstance(x, str) and x == "version":
		global version
		return version

	__setup_functions()

	from numpy import ascontiguousarray, float32
	from ctypes import POINTER, c_float
	X = ascontiguousarray(x, dtype=float32)
	P = X.ctypes.data_as(POINTER(c_float))
	__foo(P, X.size)
	return X


def __export_foo():
	import sys
	sys.modules[__name__] = foo


version = 1
__export_foo()
