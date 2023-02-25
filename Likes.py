# # import asyncio
# # import re
# # import os
# # import time
# # from selenium import webdriver
# # from selenium.webdriver import Keys
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.options import Options
# #
# # fb_post = input("Enter Post Link: ")
# #
# #
# # async def urls_of_profiles(driver):
# #     href_set = set()
# #     comments_dict = driver.find_elements(By.XPATH, '//a[@aria-hidden="false"]')
# #     comments = set(comments_dict)
# #     for comment in comments:
# #         print(comment.get_attribute('href'))
# #         href_set.add(comment.get_attribute('href'))
# #
# #
# # async def main(true=None):
# #     os.environ['PATH'] += r"C:/SeleniumDrivers"
# #     options = Options()
# #     options.add_experimental_option('detach', True)
# #     options.add_argument('--disable-notifications')
# #     driver = webdriver.Chrome(options=options)
# #     driver.maximize_window()
# #     await asyncio.sleep(1)
# #     try:
# #         driver.get('https://www.facebook.com/login')
# #         input_email = 'lacaba1242@breazeim.com'
# #         input_password = 'jhonbonda123'
# #         driver.find_element(By.ID, 'email').send_keys(input_email)
# #         driver.find_element(By.ID, 'pass').send_keys(input_password)
# #         driver.find_element(By.ID, "loginbutton").click()
# #         time.sleep(5)
# #
# #         driver.get(fb_post)
# #         await asyncio.sleep(1)
# #         likes_button = driver.find_element(By.XPATH, '//span[@class="xt0b8zv x1jx94hy xrbpyxo xl423tq"]')
# #         likes_button.click()
# #         driver.implicitly_wait(10)
# #
# #         # last_id = None
# #         #
# #         # def scroll():
# #         while True:
# #             driver.implicitly_wait(5)
# #             xpath_for_like_ids = '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 ' \
# #                                  'x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 ' \
# #                                  'xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"]'
# #             profile_links = driver.find_elements(By.XPATH, xpath_for_like_ids)
# #             profile_links_set = set(profile_links)
# #             for id in profile_links_set:
# #                 profile_link =id.get_attribute('href')
# #
# #                 result = re.search("id=([0-9]+)", profile_link)
# #                 if result:
# #                     out_put_id = result.group(1)
# #                     print(out_put_id)
# #             print(len(profile_links))
# #             last_id = profile_links[-1]
# #             driver.execute_script("arguments[0].scrollIntoView(true);", last_id)
# #             time.sleep(2)
# #             lastId = driver.find_elements(By.XPATH, xpath_for_like_ids)
# #             if profile_links[-1] == lastId[-1] and id.get_attribute('href') == lastId[-1].get_attribute('href'):
# #                 break
# #
# #     except Exception as e:
# #         print(f"Error: {e}")
# #     finally:
# #         await asyncio.sleep(1)
# #         driver.quit()
# #
# #
# # if __name__ == '__main__':
# #     asyncio.run(main())
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
# def get_fb_user_id(url):
#     # Make a request to the Facebook profile URL
#     response = requests.get(url)
#
#     # Use BeautifulSoup to parse the HTML content of the page
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Find the script tag that contains the id= value
#     script_tag = soup.find("script", text=re.compile("\"entity_id\""))
#
#     # Extract the value of the id= parameter
#     user_id = re.search('"entity_id":"([^"]+)', script_tag.text).group(1)
#
#     return user_id
#
# # Example usage
# fb_profile_url = "https://www.facebook.com/
# user_id = get_fb_user_id(fb_profile_url)
# print(user_id)