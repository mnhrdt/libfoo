
from setuptools.command.build_ext import build_ext
class my_build(build_ext):
	def run(self):
		o = "-O3 -march=native -shared -fPIC" # compilation options
		e = "so"                              # .ext of shared objects
		import sys, os
		if sys.platform == "darwin":
			e = "dylib"
			o = f"{o} -undefined dynamic_lookup"
		os.system(f"cc {o} foo.c -o cfoo.{e}")
		os.system(f"cp cfoo.{e} {self.build_lib}/cfoo.{e}")

from setuptools import Extension, setup
setup(
	name="foo",
	version="1",
	py_modules=["foo"],
	ext_modules=[ Extension(name="foo", sources=["foo.c"]) ],
	cmdclass={'build_ext': my_build}
)
