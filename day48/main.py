from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    terms = driver.find_element(
        By.XPATH, value="/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p"
    )
    terms.click()
except:
    print("terms of use already accepted")

try:
    lang = driver.find_element(By.XPATH, value='//*[@id="langSelect-PL"]')
    lang.click()
except:
    print("lang already choosed")

sleep(5)

cookie = driver.find_element(By.ID, value="bigCookie")
timer = 0
play_time = 0
while True:
    cookie.click()
    sleep(0.2)
    timer += 1
    if timer >= 15:
        try:
            enabled_items = driver.find_elements(
                By.CSS_SELECTOR, value=".product.unlocked.enabled"
            )
            enabled_items[-1].click()
        except:
            pass
        timer = 0
        play_time += 1
    if play_time > 150:
        break
    try:
        delete_achievments = driver.find_element(
            By.XPATH, value='//*[@id="notes"]/div[3]'
        )
        delete_achievments.click()
    except:
        pass

driver.quit()
