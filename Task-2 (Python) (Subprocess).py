import subprocess

command = "ls -l" 
output = subprocess.check_output(command, shell=True, text=True)
result = output.strip()

print(result)
