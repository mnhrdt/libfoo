import sys
import subprocess
from pathlib import Path
from wheel.wheelfile import WheelFile
from packaging.tags import sys_tags

def get_requires_for_build_wheel(config_settings=None):
	return ["wheel"]

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
	name = "libfoo"
	version = "0.1"
	tag = next(sys_tags())
	W = f"{name}-{version}-{tag.interpreter}-{tag.abi}-{tag.platform}.whl"

	L = "libfoo.so" if sys.platform != "darwin" else "libfoo.dylib"
	subprocess.check_call(["gcc", "-shared", "-fPIC", "-o", L, "foo.c"])

	D = f"{name}-{version}.dist-info"
	Path(D).mkdir(exist_ok=True)
	Path(D, "METADATA").write_text(f"Name: {name}\nVersion: {version}\n")
	Path(D, "WHEEL").write_text(
		"Wheel-Version: 1.0\nGenerator: custom\nRoot-Is-Purelib: false\n"
		f"Tag: {tag.interpreter}-{tag.abi}-{tag.platform}\n")

	with WheelFile(Path(wheel_directory) / W, 'w') as wf:
		wf.write("foo.py", arcname="foo.py")
		wf.write(L, arcname=L)
		wf.write(f"{D}/METADATA", arcname=f"{D}/METADATA")
		wf.write(f"{D}/WHEEL", arcname=f"{D}/WHEEL")

    return W
