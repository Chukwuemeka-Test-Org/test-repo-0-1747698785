import subprocess
def run_cmd(cmd):
    subprocess.call(cmd, shell=True)  # ⚠️ CodeQL flags this as risky
