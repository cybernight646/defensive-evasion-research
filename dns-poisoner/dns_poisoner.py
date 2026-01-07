import subprocess
import os

# Change directory to the location of the hosts file
os.chdir(r"C:\Windows\System32\drivers\etc")

# Add a record to the hosts file
command = 'echo 143.190.140.30 www.google.com >> hosts'
subprocess.run(command, shell=True, check=True)

# Flush DNS cache
command = 'ipconfig /flushdns'
subprocess.run(command, shell=True, check=True)
