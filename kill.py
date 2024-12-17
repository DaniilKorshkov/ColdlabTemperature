import subprocess


def killpython():
    raw = str(subprocess.run([f"ps","-e"], capture_output=True).stdout)
    rawlist = raw.split()
    pythonid = rawlist.index("python3\\n")
    subprocess.run(["kill",f"{rawlist[pythonid-3]}"])


killpython()