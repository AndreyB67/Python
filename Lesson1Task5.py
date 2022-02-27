import platform
import subprocess
from chardet import detect
import locale


urls = ['yandex.ru', 'youtube.com']
param = '-n' if platform.system().lower()== 'windows' else '-c'


for url in urls:
    args = ['ping', param, '4', url]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        res = detect(line)
        print('result =', res)
        line = line.decode(res['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


