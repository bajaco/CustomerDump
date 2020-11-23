from subprocess import Popen, PIPE
from pathlib import Path
import site
import json

set_process = Popen(['env'], stdout=PIPE)
output = set_process.communicate()

data = {}

env = {}
for term in output[0].decode().split():
    parts = term.split('=') 
    env[parts[0]] = ''.join(parts[1:])

system_packages = []
user_packages = []
for path in site.getsitepackages():
    pkg_path = Path(path)
    for p in pkg_path.glob('*'):
        system_packages.append(str(p))
pkg_path = Path(site.getusersitepackages())
for p in pkg_path.glob('*'):
    user_packages.append(str(p))

installed_process = Popen(['apt list --installed'], shell=True, stdout=PIPE)
output = installed_process.communicate()

installed = output[0].decode().splitlines()

data['customer'] = input('Name: ')
data['contact'] = input('Best Method of Contact: ')
data['issue'] = input('Brief description of your issue: ')
data['environment'] = env
data['packages'] = {}
data['packages']['python-user'] = user_packages
data['packages']['python-system'] = system_packages
data['packages']['ubuntu'] = installed

out = json.dumps(data, indent=4)
with open('customer-data.json', 'w') as f:
    f.write(out)
