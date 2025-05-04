import os
import sys
from packaging.tags import sys_tags

def get_requires_for_build_wheel(config_settings=None):
	return ["wheel"]

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
	name = "libfoo"
	version = "1"
	tag = next(sys_tags())
	wheel_filename = f"{name}-{version}-{tag.interpreter}-{tag.abi}-{tag.platform}.whl"

	lib_name = "libfoo.so" if sys.platform != "darwin" else "libfoo.dylib"
	os.system(f"gcc -shared -fPIC -o {lib_name} foo.c")

	dist_info_dir = f"{name}-{version}.dist-info"
	os.system(f"mkdir -p {dist_info_dir}")
	os.system(f'echo "Name: {name}\nVersion: {version}" > {dist_info_dir}/METADATA')
	os.system(f'echo "Wheel-Version: 1.0\nGenerator: custom\nRoot-Is-Purelib: false\nTag: {tag.interpreter}-{tag.abi}-{tag.platform}" > {dist_info_dir}/WHEEL')
	os.system(f"tar -cf {wheel_filename} foo.py {lib_name} {dist_info_dir}")
	os.system(f"mv {wheel_filename} {wheel_directory}")
	return wheel_filename

