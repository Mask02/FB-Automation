import asyncio
import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import re
from time import sleep

# **************************************************
input_email = 'lacaba1242@breazeim.com'
input_password = 'jhonbonda123'

# **************************************************

fb_post = input("Enter Post Link: ")

res = []


def get_id_from_username(url):
    # print(url)
    id1 = None
    response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")
    # script = soup.find('script')
    # print(script)
    # if script:
    #     script_text = script.text
    #     match = re.search(r'id=(\d+)', script_text)
    #     if match:
    #         id = match.group(1)
    #         print('id:', id)

    soup = BeautifulSoup(response.content, "html.parser")
    # meta_tags = soup.find_all("meta")
    meta_tag = soup.find("meta", attrs={"property": "al:android:url"})
    # print(meta_tag)
    if meta_tag:
        id1 = re.findall(r"\d+", meta_tag["content"])[0]
    else:
        meta_tag = soup.find("meta", attrs={"property": "al:ios:url"})
        if meta_tag:
            id1 = re.findall(r"\d+", meta_tag["content"])[0]
            # print(id1)

    return id1


async def urls_of_profiles(driver):
    driver.implicitly_wait(2)
    comments_dict = driver.find_elements(By.XPATH, '//a[@aria-hidden="false"]')
    comments = set(comments_dict)

    print(len(comments_dict), len(comments))

    for comment in comments:
        out_put_id = None
        comments_urls = comment.get_attribute('href')
        result = re.search("id=([0-9]+)", comments_urls)
        # print(comments_urls, result)
        if result:
            out_put_id = result.group(1)

        else:
            match = re.search(r"^.*\?", comments_urls)
            if match:
                username_url = match.group(0)[:-1]
                out_put_id = get_id_from_username(username_url)
                # print(username_url)
        if out_put_id:
            print(out_put_id)
            res.append(out_put_id)
    print(len(res))


async def main(true=None):
    # os.environ['PATH'] += r"C:/SeleniumDrivers"
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    await asyncio.sleep(1)
    try:
        driver.get('https://www.facebook.com/login')
        driver.find_element(By.ID, 'email').send_keys(input_email)
        sleep(1)
        driver.find_element(By.ID, 'pass').send_keys(input_password)
        sleep(1)
        driver.find_element(By.ID, "loginbutton").click()
        time.sleep(2)

        driver.get(fb_post)
        time.sleep(2)
        driver.find_element(By.XPATH, '//div[div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 '
                                      'x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 '
                                      'x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m '
                                      'x1n2onr6 x87ps6o x1lku1pv x1a2a7pz"]]').click()
        driver.implicitly_wait(2)
        driver.find_elements(By.XPATH, '//div[span[contains(text(),"All comments")]]')[0].click()
        driver.implicitly_wait(4)
        # scroll_element = driver.find_element(By.XPATH,
        #                                      '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 '
        #                                      'x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x '
        #                                      'xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa x2b8uid"]')

        driver.implicitly_wait(2)

        while True:
            try:
                time.sleep(1)
                driver.implicitly_wait(5)
                try:
                    time.sleep(1)
                    scroll_element = driver.find_element(By.XPATH,
                                                         '//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 '
                                                         'x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x '
                                                         'xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa x2b8uid"]')
                    driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
                    time.sleep(1)
                    driver.implicitly_wait(2)
                    driver.find_element(By.XPATH, '//*[contains(text(),"more comments")]').click()
                except:
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(1)
                    driver.implicitly_wait(10)
                    driver.find_element(By.XPATH, '//*[contains(text(),"more comments")]').click()

                # time.sleep(1)
                # # comments_dict = driver.find_elements(By.XPATH, '//a[@aria-hidden="false"]')
                # # comments = set(comments_dict)
                # # for comment in comments:
                # #     href_set.add(comment.get_attribute('href'))
                # driver.find_element(By.XPATH, '//*[contains(text(),"more comments")]')
            except:
                try:
                    previous_comment = driver.find_element(By.XPATH, '//*[contains(text(),"previous comments")]')
                    if previous_comment:
                        previous_comment.click()
                    else:
                        print('f')
                except:
                    print('oy')
                    break

        await urls_of_profiles(driver)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("done")
        await asyncio.sleep(1)
        # driver.quit()


if __name__ == '__main__':
    asyncio.run(main())
