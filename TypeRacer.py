from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def wait_until(driver, by: By, name: str):
        element = None
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((by, name))
            )
        except:
            print("WebDriverWait timed out: couldn't find " + name)
            exit()
        return element

def wait_attr(driver, Element):
    try:
        element = Element.find_element_by_css_selector("input")
    except NoSuchElementException:
        return False
    a = element.get_attribute("disabled")
    return a == "false" or a == "" or a == None 

def race(driver):
	# webdriver.ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys("I").key_up(Keys.CONTROL).key_up(Keys.ALT).build().perform()
    EnterTypeRacing = wait_until(driver, By.XPATH, '//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a')
    webdriver.ActionChains(driver)\
        .move_to_element(EnterTypeRacing)\
        .click(EnterTypeRacing)\
        .perform()

    TrafficLight = wait_until(driver, By.XPATH, '/html/body/div[5]')
    Table = wait_until(driver, By.CLASS_NAME, "inputPanel")
    all_text = Table.find_elements_by_tag_name('span')
    InputBox = Table.find_element_by_css_selector("input")

    whole_text = ""
    if(len(all_text)>2):
        whole_text += (all_text[0].text + all_text[1].text + " " + all_text[2].text)
    else:
        whole_text += (all_text[0].text + " " + all_text[1].text)
    # for child in all_text:
    #     if(child.text == "" or child.text == None):
    #         whole_text += " "
    #     else:
    #         whole_text += child.text
    # print(whole_text)
    
    while(wait_attr(driver, Table) == False):
        pass

    for c in whole_text:
        if( c == " " ):
            InputBox.send_keys(Keys.SPACE)
        else:
            InputBox.send_keys(c)
        time.sleep(0.015)
    
    time.sleep(5)
    driver.refresh()
    race(driver)


def start_hacking():
    option = webdriver.ChromeOptions()
    # option.add_argument(" — incognito")
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=option)

    driver.get("https://play.typeracer.com/")
    # time.sleep(10)
    
    race(driver)



start_hacking()