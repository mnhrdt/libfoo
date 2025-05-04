
from setuptools.command.build_py import build_py
class my_build(build_py):
	def run(self):
		from os import system as sh
		sh("cc -O3 -march=native -shared -fPIC foo.c -o libfoo.so")
		super().run()
		sh(f"cp libfoo.so {self.build_lib}/libfoo.so")

from setuptools import setup
setup(
	name="foo",
	version="1",
	py_modules=["foo"],
	cmdclass={'build_py': my_build},
)
