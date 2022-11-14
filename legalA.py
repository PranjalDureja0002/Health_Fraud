from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd


def date_sel(date,mnth,year):
    selectMonth = driver.find_element_by_xpath('/html/body/div[6]/div/div/select[1]')
    for option in selectMonth.find_elements_by_tag_name('option'):
        if option.text==mnth:
            option.click()
            print("d")
            break
    driver.implicitly_wait(10)
    selectYear = driver.find_element_by_xpath('/html/body/div[6]/div/div/select[2]')
    for option in selectYear.find_elements_by_tag_name('option'):
        if option.text==year:
            option.click()
            print("g")
            break
    
    days = driver.find_elements_by_xpath("/html/body/div[6]/table//a[@class='ui-state-default']")
    print(days)
    days[date-1].click()



url = 'https://main.sci.gov.in/daily-order'

# initialize Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')
#driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome('D:/chromedriver.exe',options=options)



# open website
driver.get(url)

# maximize window
driver.maximize_window()

#driver.find_element_by_xpath("//select[@id='sess_dist_code']/option[text()='Pune-पुणे ']").click()
#driver.find_element_by_xpath("//a[@href='javascript:void(0)' and text()='Court Orders']").click()


# driver.find_element(By.XPATH,"//a[@href='/daily-order']").click()

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/ul[2]/li[3]/a").click()
# driver.switch_to.frame(driver.find_element(By.ID,"JBJfrom_date").click())


# #a = driver.find_element_by_xpath("//a[@class='z-link' and text()='ROP Date']").click()
# driver.find_element_by_xpath("//*[@id='tabbed-nav']/ul/li[3]").click()
# print("a")

#sdate_val = '01-01-2022'
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='JBJfrom_date']").click()
#sdate = driver.find_element_by_xpath("//input[@id='JBJfrom_date']")

date_sel(5,"Mar","2022")

driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='JBJto_date']").click()
#sdate = driver.find_element_by_xpath("//input[@id='JBJfrom_date']")

date_sel(15,"Mar","2022")
# sdate.send_keys(sdate_val)

# fdate_val = '04-01-2022'
# driver.implicitly_wait(10)
# sdate = driver.find_element_by_xpath("//input[@id='JBJto_date']").clear()
# sdate = driver.find_element_by_xpath("//input[@id='JBJto_date']")

# sdate.send_keys(fdate_val)

cap_text = driver.find_element_by_id("cap").find_element_by_tag_name("font").text

driver.find_element_by_xpath('//*[@id="ansCaptcha"]')

s = driver.find_element_by_id("ansCaptcha")
s.send_keys(cap_text)

driver.find_element_by_id("getJBJ").click()
driver.implicitly_wait(20)
rec = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/table")

content = rec.get_attribute("outerHTML")

df = pd.read_html(content)
df[0].to_csv("Supreme_Data.csv",index=False)
# in_text = '01-01-2022'
# sdate = driver.find_element_by_xpath("//table[@class='mobview']/tbody/tr/td[@data-label='Between dates']/input[@id='JBJfrom_date']")
# sdate.send_keys(in_text)

# sdate.send_keys(sdate_val)


# driver.find_element_by_xpath("//*[@id='JBJto_date']")

#20 seconds 