import time

from random import randint, choice
from selenium.webdriver.common.by import By

from selenium import webdriver

#password generation
def password():
    a = []
    alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for i in range(8):
        a.append(choice(alphabet))
    num = randint(0, 10)
    a.append(str(num))
    return (''.join([*a])).title()


ent_pass = password()
driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
driver.get("https://dev3.freento.com/")
driver.maximize_window()
time.sleep(1)
element = driver.find_element(By.ID, "idWiJwHefh")
element.click()
time.sleep(1)

#create an account
firstname = driver.find_element(By.NAME, "firstname")
firstname.send_keys("Igor")
lastname = driver.find_element(By.NAME, "lastname")
lastname.send_keys("Igor")
email = driver.find_element(By.NAME, "email")
email.send_keys("test+{0}@test.com".format(randint(0, 999999)))
password = driver.find_element(By.NAME, "password")
password.send_keys(ent_pass)
password_2 = driver.find_element(By.NAME, "password_confirmation")
password_2.send_keys(ent_pass)
account = driver.find_element(By.XPATH, """//*[@id="form-validate"]/div/div[1]/button/span""")
account.click()
time.sleep(1)

#check message
value = driver.find_element(By.XPATH, """/html/body/div[2]/main/div[1]""").is_enabled()
time.sleep(30)

driver.quit()
