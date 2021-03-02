import time
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# list of number to get random seconds
short_time = [1, 2, 2.2 ,3 ,3.5 ,4 ,5 ,4.6]
normal_time = [6, 7.1, 8, 8.7, 10, 11, 11.3 ,12, 12.9, 14]
longer_time = [18, 20, 24, 27, 36, 28.5, 16.7, 30.2, 23.87, 19.4, 33.1]

in_user = input("Enter username/email :")
in_pass = input("Enter password : ")

times = int(input("How man times you want the code to run  [max:10]  : "))
t = 0

if t <= 10:
    pass

elif t > 10:
    quit()

else:
    print("try again.......")
    quit()

# path for the chrome file
path = "C:\Program Files (x86)\chromedriver.exe"
# choosing web browser
driver = webdriver.Chrome(path)

print("Opening instagram")
time.sleep(1)



# going to login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(random.choice(short_time))

# finding username
username = driver.find_element_by_name("username")
# finding password
password = driver.find_element_by_name("password")

# sending keys
username.send_keys(in_user)
password.send_keys(in_pass)
time.sleep(random.choice(short_time))
login = driver.find_element_by_xpath("//*[text()='Log In']")
login.click()
time.sleep(random.choice(short_time))


# here is list of people to whom we will follow
# you can add some by yourself ;)
to_follow = ["https://www.instagram.com/cristiano/", "https://www.instagram.com/leomessi/", "https://www.instagram.com/sidhu_moosewala/", ]


def follow_them():
    print("[*]--------------------[*]")
    global t
    # loop to folow
    for links in to_follow:

        time.sleep(random.choice(normal_time))
        driver.get(links)

        try:

            # finding follow button
            follow_button = driver.find_element_by_xpath("//*[text()='Follow']")

            # click on it
            follow_button.click()
            print("followed ", links)
            time.sleep(random.choice(longer_time))
        
        except Exception as ex:
            print("================")
            print(ex)
            print('=================')

    unfollow_them()



def unfollow_them():
    print("[*]--------------------[*]")
    global t
    # loop to unfollow
    for links in to_follow:
        time.sleep(random.choice(normal_time))
        driver.get(links)

        try:

            # finding following logo
            tick_button = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div[1]'
            # finding unfollow option
            other_button = "//*[text()='Unfollow']"
            
            time.sleep(random.choice(short_time))
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div[1]').click()

            print("clicked on logo")

            time.sleep(1)
            driver.find_element_by_xpath(other_button).click()

            print("unfollowed ", links)
            time.sleep(random.choice(longer_time))
  

        except Exception as a:

            print(a)
        
    t += 1 
    checker()


def checker():

    if t == times:
        driver.quit()
        quit()

    else:
        time.sleep(7)
        follow_them()

follow_them()