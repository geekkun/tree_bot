# -*- coding: utf-8 -*-
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
import rstr
import time
import os.path

browser = webdriver.Firefox()

browser.get('')

postcode_reg = "[ ]*([a-zA-Z]{1,2}[0-9Rr][0-9a-zA-Z]?)[ ]*([0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2})[ ]*"

n = 'E15JS'

def stopWatch(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)

    valueMS = (valueS - Seconds)*1000
    MSec = int(valueMS)

    print Seconds,":",MSec
    return Seconds

start = time.time()

# ADD REDO FOR INCORRECT POSTCODE
def postcode(n):
    posty = n
    pattern = re.compile(postcode_reg)
    pattern.match(posty)
    return posty.upper()


def postcode_gen(n):
    postcoded = n
    a = randint(0,9)
    rs = rstr.xeger('[abd-hjlnp-uw-zABD-HJLNP-UW-Z]')
    r = rstr.xeger('[abd-hjlnp-uw-zABD-HJLNP-UW-Z]')
    postcoded += " "+str(a)+rs+r
    return postcoded

def waiter(n):
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, n))
    )


def click(n):
    waiter(n)
    browser.find_element_by_xpath(n).click()


def type(n, j):
    waiter(n)
    browser.find_element_by_xpath(n).send_keys(j + Keys.RETURN)


def select(n, j):
    click(n)
    mySelect = Select(browser.find_element_by_xpath(n))
    mySelect.select_by_visible_text(j)


def pics(pat, type, max):
    # click(".//*[@id='post-ad-container']/div[6]/div/div/div[1]/ul/li/a") # not needed
    path = pat + type + str(randint(1, max)) + ".jpg"
    browser.find_element_by_css_selector("input[type=\"file\"]").send_keys(path)


# new user
click(".//*[@id='#login-post-ad']/form/button")

# category TAKES AGES
try:
    type(".//*[@id='post-ad_title-suggestion']", 'room')
except:
    alert = browser.switch_to.alert
    alert.accept()
    type(".//*[@id='post-ad_title-suggestion']", 'room')

click(".//*[@id='post-ad-container']/div/div/div/div[1]/div[2]/section/div[2]/button")

# postcode
type(".//*[@id='post-ad_postcode']", postcode(postcode_gen("E1")) + Keys.RETURN)

# no map
try:
    click(".//*[@id='post-ad-container']/div[2]/div[1]/div/div[1]/div[2]/label")
except:
  pass

# agent
click(".//*[@id='post-ad-container']/div[3]/div/div/div/div/div/div/div/div[1]/div/label")

nice = []
room = []
stations = []
price = []
texts = ['', '', '']
ending = ''
phone = ''
name = ''
priceN = randint(0,len(nice)-1)

phrase = nice[randint(0,len(nice)-1)] + ' ' + room[randint(0,len(room)-1)] + ' room near ' + stations[randint(0,len(room)-1)] \
         + ' just for ' + price[priceN] + 'pw' + phone

desc = []

type(".//*[@id='post-ad_title']", phrase)  # title

type(".//*[@id='description']", desc[randint(0,len(desc)-1)] + ending)  # description

type(".//*[@id='price']", price[priceN])  # price

# calendar
click(".//*[@id='available_date']")
click(".//*[@id='available_date_table']/tbody/tr[3]/td[4]/div")

# property
select(".//*[@id='property_number_beds']", "3")
select(".//*[@id='property_type']", "Flat")

# personal details
# click(".//*[@id='post-ad-container']/div[10]/div/div[1]/div[1]/label")
# click(".//*[@id='post-ad-container']/div[10]/div/div[2]/div/div/div[1]/label")
#
# type(".//*[@id='post-ad_contactTelephone']",phone)
# type(".//*[@id='post-ad_contactName']","")
# type(".//*[@id='post-ad_contactName']",name)



# add photos
try:
    path = r""   #Enter your path
    browser.find_element_by_css_selector("input[type=\"file\"]").send_keys(path)
except Exception, e:
    print "Sorry, no pic for you"
    print str(e)
    pass
# pics("/Users/kuznetsov/Documents/rooms/fake/","bed",29)

# path = "/Users/kuznetsov/Documents/rooms/fake/bath1.jpg"   #Enter your path
# browser.find_element_by_css_selector("input[type=\"file\"]").send_keys(path)


try:
    pics("","bath",16)
except Exception, e:
    print "Sorry, no pic for you"
    print str(e)
    pass

end = time.time()

if(stopWatch(end-start) < 15) :
    print "FAST"
