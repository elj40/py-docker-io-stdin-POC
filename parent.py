from subprocess import Popen, PIPE, STDOUT

# Using subprocess means you can only get printed text at the end of the process
# This means you have type your inputs blind
# Shouldnt be a problem since because acual UI is done elsewhere, we just need top pass in data

command = ["docker","run","-i","pythonio"]
#command = ["python3","app.py"]
command_str = ' '.join(command)
print('Running: ' + command_str)

program = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

output, errors = program.communicate(input='asdf\nghjk\nbnm')

print('===============================================================')
print("stdout: " + output) # Output
print('===============================================================')
print("stderr: " + errors) # Errors
print('===============================================================')


