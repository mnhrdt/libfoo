
from setuptools.command.build_ext import build_ext
class my_build(build_ext):
	def run(self):
		from os import system as SH
		SH(f"cc -O3 -march=native -shared -fPIC foo.c -o libfoo.so")
		SH(f"cp libfoo.so {self.build_lib}/libfoo.so")

from setuptools import Extension, setup
setup(
	name="foo",
	version="1",
	py_modules=["foo"],
	ext_modules=[ Extension(name="foo", sources=["foo.c"]) ],
	cmdclass={'build_ext': my_build}
)
