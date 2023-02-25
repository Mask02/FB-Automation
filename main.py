import time
import os
import option as option
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

os.environ['PATH'] += r"C:/SeleniumDrivers"
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=options)
options.add_argument("--start-maximized")

# driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Accessible login button"]').click()
# driver.implicitly_wait(15)
# driver.back()
# driver.back()
# driver.back()
# driver.get('https://www.facebook.com/login/?__tn__=*F')
# driver.find_elements(By.CLASS_NAME,)
# profile_urls = driver.find_elements(By.CSS_SELECTOR, 'a[aria-hidden="true"]')
//div[a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]]


# sample profile Urls for testing
"""
https://www.facebook.com/StartupPakistanSP/photos/a.1087939834659273/5754316334688243/
https://www.facebook.com/StartupPakistanSP/photos/a.1087939834659273/5773248779461665/

"""



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
176.31.200.104:3128,
83.77.118.53:17171,
173.192.21.89:80,
163.172.182.164:3128,
163.172.168.124:3128,
164.68.105.235:3128,
5.199.171.227:3128,
93.171.164.251:8080,
212.112.97.27:3128,
51.68.207.81:80,
91.211.245.176:8080,
84.201.254.47:3128,
95.156.82.35:3128,
185.118.141.254:808,
164.68.98.169:9300,
217.113.122.142:3128,
188.100.212.208:21129,
83.77.118.53:17171c,
83.79.50.233:64527
]
