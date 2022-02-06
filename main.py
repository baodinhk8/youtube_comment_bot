from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random

# chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get(
#     "CHROMEDRIVER_PATH"), chrome_options=chrome_options)


driver = webdriver.Chrome('./chromedriver')
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

gmail_name = driver.find_element_by_name("identifier")
for letter in "dsuLidNkeI@gmail.com":
    gmail_name.send_keys(letter)
    wait_time = random.randint(0, 1000)/1000
gmail_name.send_keys(Keys.RETURN)

time.sleep(3)

passwords = driver.find_element_by_name("password")
for letter in "Giabaok8":
    passwords.send_keys(letter)
    wait_time = random.randint(0, 1000)/1000
passwords.send_keys(Keys.RETURN)

time.sleep(5)


while 1:

    driver.find_element_by_xpath('//*[@id="video-title"]').click()

    time.sleep(5)

    driver.execute_script('window.scrollTo(0,(window.pageYOffset+5000))')

    time.sleep(2)

    my_comment_list = ["Very nice video, I like it.",
                       "Cool video", "I love it, but can you please make it more interesting? Thanks!", "Interesting...", "it's not a mistake ✨ it's a masterpiece ✨ ", "This is the coolest video i have ever seen @@", "Nice videooooooo", "Do you want to be my friend, i have no friend :(", "THE VIDEO IS GOOD BUT I WANT A SUBCRIBEEEE"]

    my_comment = random.choice(my_comment_list)

    try:
        comment_box = driver.find_element_by_xpath('//*[@id="content"]')
        a = ((((str(comment_box.text)).split("SORT BY"))[1]).split(
            "REPLY"))[random.choice([4, 5, 6, 7, 8])].split("\n")
        if (a[4] != '' and not(a[4].isnumeric())):
            my_comment = a[4]
        else:
            my_comment = a[3]
    except:
        pass

    my_comment = my_comment + \
        " p/s: please give me a subcribeee"

    print(my_comment)

    try:

        comment_input = driver.find_element_by_css_selector(
            "ytd-comment-simplebox-renderer")

        entering_comment_actions = ActionChains(driver)

        entering_comment_actions.move_to_element(comment_input)
        entering_comment_actions.click()

        for letter in my_comment:
            entering_comment_actions.send_keys(letter)
            wait_time = random.randint(0, 1000)/1000
            entering_comment_actions.pause(wait_time)

        entering_comment_actions.perform()

        time.sleep(2)

        send_comment_button = driver.find_element_by_id("submit-button")
        send_comment_button.click()
    except:
        pass

    time.sleep(5)

    driver.get("https://www.youtube.com/")

    time.sleep(5)
