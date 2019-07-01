
import requests
import time

url = 'https://jsj.nielscloud.cn/file/manual'
f = open('links2.txt')
lines = f.readlines()
print(len(lines))
for line in lines:
    if line.startswith('http'):
        link = line.rstrip('\n')
        requests.post(url, json={"fileLink": link})
        print(link)
        time.sleep(6)
f.close