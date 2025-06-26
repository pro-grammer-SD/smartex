from subprocess import run
from glob import glob

run("hatch build", shell=True, check=True)

wheels = glob("dist/smartex-*.whl")
if not wheels:
    raise FileNotFoundError("❌ No .whl file found in dist/")
whl_path = wheels[0]

run(f"pip install {whl_path}", shell=True, check=True)

# 💡 Instead of relying on PATH, call CLI module directly
run("python -m smartex \"\\int_0^1 x^2 dx\" -o integral -s Huge", shell=True, check=True)
