import re
import subprocess

HOST_IP = '139.59.169.246'
HOST_PORT = '8080'

p = subprocess.Popen(f'netselect -vv {HOST_IP}:{HOST_PORT}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
string_returned = p.stdout.read().decode()
parsed = re.findall(r'[\d.]+:+[\d]+\s+[\d]+\sms', string_returned)[0]
proxy = re.findall(r'[\d.]+:+[\d]+', parsed)[0]
speed = re.findall(r'[\d]+\sms', parsed)[0]

print(f'PROXY: {proxy} with speed {speed}')
