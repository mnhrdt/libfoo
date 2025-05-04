from setuptools import setup
from setuptools.command.build_py import build_py
import subprocess
import shutil

class BuildWithCLib(build_py):
	def run(self):
		subprocess.check_call(['gcc', '-shared', '-o', 'libfoo.so', '-fPIC', 'foo.c'])
		super().run()
		build_lib_path = self.build_lib
		target_path = os.path.join(build_lib_path, 'libfoo.so')
		shutil.copyfile('libfoo.so', target_path)

setup(
	name='foo',
	version='0.1',
	py_modules=['foo'],
	package_data={'': ['libfoo.so']},
	include_package_data=True,
	cmdclass={'build_py': BuildWithCLib},
)
