import asyncio
import re
import os
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import re

fb_post_url = input("Enter Post Link: ")
fb_post = fb_post_url.replace('www', 'm')


def get_id_from_username(url):
    id_1 = None
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # meta_tags = soup.find_all("meta")
    meta_tag = soup.find("meta", attrs={"property": "al:android:url"})
    if meta_tag:
        id_1 = re.findall(r"\d+", meta_tag["content"])[0]
    else:
        meta_tag = soup.find("meta", attrs={"property": "al:ios:url"})
        if meta_tag:
            id_1 = re.findall(r"\d+", meta_tag["content"])[0]

    return id_1


async def urls_of_profiles(driver):
    user_ids = set()
    likes_button = driver.find_elements(By.XPATH, '//a[@class="darkTouch _1aj5 l"]')
    # print(likes_button)
    likes_button_url = set(likes_button)
    for id1 in likes_button_url:
        result = id1.get_attribute('href')
        # print(result)
        result_1 = re.search("id=([0-9]+)", result)
        if result_1:
            out_put_id = result_1.group(1)
            print(out_put_id)
        # else:
        #     match = re.search(r"^.*\?", id1)
        #     if match:
        #         username_url = match.group(0)[:-1]
        #         out_put_id = get_id_from_username(username_url)

            if out_put_id:
                print(out_put_id)
                user_ids.add(out_put_id)

        print("total:", len(user_ids))


async def main(true=None):
    os.environ['PATH'] += r"C:/SeleniumDrivers"
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    action = ActionChains(driver)
    # driver.maximize_window()
    await asyncio.sleep(1)
    try:
        driver.get('https://www.facebook.com/login')
        input_email = 'pecic82088@mustbeit.com'
        input_password = '63546rfjghvjygi97uty987y9'
        driver.find_element(By.ID, 'email').send_keys(input_email)
        driver.find_element(By.ID, 'pass').send_keys(input_password)
        driver.find_element(By.ID, "loginbutton").click()
        time.sleep(5)

        driver.get(fb_post)
        await asyncio.sleep(1)
        # likes_button = driver.find_element(By.XPATH, '//span[@class="xt0b8zv x1jx94hy xrbpyxo xl423tq"]')
        likes_button_link = driver.find_element(By.XPATH, '//a[@class="_45m8"]')
        action.click(likes_button_link)
        action.perform()
        driver.implicitly_wait(10)
        while True:
            try:
                see_more = driver.find_element(By.ID, 'reaction_profile_pager')
                see_more.click()
                time.sleep(2)
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            except:
                print('oy')
                break
        await urls_of_profiles(driver)
    #  for likes in likes_button:
    #      profile_link = likes.get_attribute('href')
    # # last_id = None
    #
    # def scroll():
    # user_ids = set()
    # while True:
    #     await asyncio.sleep(3)
    #     driver.implicitly_wait(10)
    #     xpath_for_like_ids = '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 ' \
    #                          'x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 ' \
    #                          'xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]'
    #     profile_links = driver.find_elements(By.XPATH, xpath_for_like_ids)
    #     profile_links_set = set(profile_links)
    #     print(len(profile_links))
    #     # print(len(profile_links))
    #     last_id = profile_links[-1]
    #     print(last_id)
    #     driver.execute_script("arguments[0].scrollIntoView(true);", last_id)
    #     time.sleep(2)
    #     lastid = driver.find_elements(By.XPATH, xpath_for_like_ids)
    #     print(lastid[-1])
    # await asyncio.sleep(3)
    # if profile_links[-1] == lastid[-1] and profile_links[-1].get_attribute('href') == lastid[-1].get_attribute(
    #         'href'):
    # for id1 in profile_links_set:
    #     profile_link = id1.get_attribute('href')
    #
    # result = re.search("id=([0-9]+)", profile_link)
    # if result:
    #     out_put_id = result.group(1)
    #
    # else:
    #     match = re.search(r"^.*\?", profile_link)
    #     if match:
    #         username_url = match.group(0)[:-1]
    #         out_put_id = get_id_from_username(username_url)
    #
    # if out_put_id:
    #     print(out_put_id)
    #     user_ids.add(out_put_id)
    #
    # print("total:", len(user_ids))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await asyncio.sleep(1)
        driver.quit()


if __name__ == '__main__':
    asyncio.run(main())

# loop break handling with 10 time check and exception handlinng
