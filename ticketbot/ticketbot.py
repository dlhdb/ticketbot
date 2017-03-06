from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import digitRecognize as dRcg

# initial WebDriver
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')

# connect to website
browser.get('http://railway.hinet.net/ctkind1.htm')

# fill booking info
persion = browser.find_element_by_xpath("//*[@id='person_id']")
persion.send_keys('A172005729')

from_station = browser.find_element_by_xpath("//*[@id='from_station']")
from_station.send_keys('096' + Keys.RETURN)

to_station = browser.find_element_by_xpath("//*[@id='to_station']")
to_station.send_keys('070' + Keys.RETURN)

date = browser.find_element_by_xpath("//*[@id='getin_date']")
date.send_keys('2017/02/28' + Keys.RETURN)

ticketNum = browser.find_element_by_xpath("//*[@id='order_qty_str']")
ticketNum.send_keys('2' + Keys.RETURN)

trainType = browser.find_element_by_xpath("//*[@id='train_type']")
trainType.send_keys('*1' + Keys.RETURN)

startTime = browser.find_element_by_xpath("//*[@id='getin_start_dtime']")
startTime.send_keys('07' + Keys.RETURN)

endTime = browser.find_element_by_xpath("//*[@id='getin_end_dtime']")
endTime.send_keys('12' + Keys.RETURN)
# submit
browser.find_element_by_xpath("/html/body/form/table/tbody/tr[11]/td[2]/button").click()


# deal with verification code
# get verification image
while(1):
    img = browser.find_element_by_xpath("//*[@id='idRandomPic']")
    src = img.get_attribute('src')
    print("verification image url : " + src)
    # get screenshot and crop by element location and size
    browser.save_screenshot("screenshot.png")
    im = Image.open('screenshot.png')
    left = 285
    top = 135
    right = 582
    bottom = 222
    im = im.crop((left, top, right, bottom))# crop image
    im.save('screenshot_crop.png') # saves new cropped image
    dRcg.digitRecg()
    browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/button[2]").click()
# recoginize verification image

# fill verification code and submit


#browser.close()

