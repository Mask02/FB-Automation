import itertools
from selenium import webdriver
import time

proxies = [
    # 145.239.85.58:9300
    # 46.4.96.137:1080
    # 47.91.88.100	1080
    # 45.77.56.114	30205
    # 82.196.11.105	1080
    # 51.254.69.243	3128
    # 178.62.193.19	1080
    # 188.226.141.127	1080
    # 217.23.6.40	1080
    # 185.153.198.226	32498
    # 81.171.24.199	3128
    # 5.189.224.84	10000
    # 108.61.175.7	31802
    '176.31.200.104:3128',
    '83.77.118.53:17171',
    '173.192.21.89:80',
    '163.172.182.164:3128',
    '163.172.168.124:3128',
    '164.68.105.235:3128',
    '5.199.171.227:3128',
    '93.171.164.251:8080',
    '212.112.97.27:3128',
    # 51.68.207.81:80,
    # 91.211.245.176:8080,
    # 84.201.254.47:3128,
    # 95.156.82.35:3128,
    # 185.118.141.254:808,
    # 164.68.98.169:9300,
    # 217.113.122.142:3128,
    # 188.100.212.208:21129,
    # 83.77.118.53:17171c,
    # 83.79.50.233:64527

]

cycle through the proxies infinitely
proxy_cycle = itertools.cycle(proxies)

for i in range(len(proxies)):
    # print(proxy)
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy)
driver = webdriver.Chrome(options=options)
driver.get('http://whatismyipaddress.com')
driver.implicitly_wait(10)
time.sleep(10)
driver.quit()
