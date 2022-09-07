import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import re

options = webdriver.ChromeOptions()
#options.binary_location = ('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
#options.add_argument("user-data-dir=C:\\Users\\Hatim\\AppData\\Local\\Google\\Chrome\\User Data\\Default") #Path to your chrome profile
driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.get("https://google.com/")
driver.maximize_window()
driver.implicitly_wait(30)
search =['+"@yahoo.com" ~ "key" -intitle:"profiles" -inurl:"dir/ " site:www.linkedin.com/in/ OR site:www.linkedin.com/pub/',
         '+"@yahoo.com" ~ "key" -intitle:"profiles" -inurl:"dir/ " site:www.ar.linkedin.com/in/ OR site:www.ar.linkedin.com/pub/']
keywords= ['Keyword1','keyword2','keyword3']
def check_next():
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Suivant')]")
    except NoSuchElementException:
        return False
    return True

for s in search:
    for k in keywords:
        driver.get("https://google.com/")
        driver.find_element(By.CSS_SELECTOR,'.gLFyf.gsfi').send_keys(s.replace("key",k))
        driver.find_element(By.CSS_SELECTOR,'.gLFyf.gsfi').send_keys(Keys.ENTER)
        time.sleep(2)
        l=driver.find_element_by_xpath("/html/body").text
        with open('Search_Result.txt', 'a',encoding="utf-8") as f:
            f.write(l+"\n")
        x = True
        while(x):
            print("Entered while loop")
            if(check_next()== False):
                print("I will break from this loop")
                break
            if(check_next()):
                print("checked if next is here")
                driver.find_element(By.XPATH, "//span[contains(text(), 'Suivant')]").click()
                time.sleep(2)
                r = driver.find_element_by_xpath("/html/body").text
                with open('Search_Result.txt', 'a',encoding="utf-8") as f:
                    f.write(r + "\n")
                print("x=true")


driver.close
with open('Search_Result.txt', 'r',encoding="utf-8") as file:
    data = file.read().replace('\n', '')



emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]+", data)
for e in emails:
    with open('Emails.txt', 'a', encoding="utf-8") as f:
        f.write(e+ "\n")
with open('Emails.txt','r',encoding="utf-8") as emailsrandom:
    for em in emailsrandom:
        with open('CleanEmails.txt','a',) as cle:
            partone,parttwo,parttree = em.partition('yahoo.com')
            cle.write(partone+"yahoo.com" + "\n")

#SJajHc NVbCr

