import subprocess

a=subprocess.check_output("ls | grep log.txt", shell=True)
print(a)
