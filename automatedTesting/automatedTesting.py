from appium import webdriver
from selenium.webdriver.common.by import By

WAIT_TIME = 5

capabilities = { 'browserName': 'Chrome', 'automationName': 'UIAutomator2', 'platformName': 'Android', 'platformVersion': '5.1' }
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)


driver.get('https://www.cathaybk.com.tw/cathaybk/')
driver.implicitly_wait(WAIT_TIME)
driver.save_screenshot('./images/login/login.png')
screenshot = 1

driver.find_element(By.CLASS_NAME, 'cubre-o-header__burger').click()
driver.find_element(By.XPATH, '//div[3]/div/div[2]/div/div/div/div/div').click()
driver.find_element(By.XPATH,'//div[2]/div/div/div/div[2]/div/div/div/div').click()
driver.implicitly_wait(WAIT_TIME)
driver.save_screenshot('./images/creditCard/creditCardList.png')
screenshot += 1

list = driver.find_elements(By.XPATH, "//div[contains(@class,'is-L2open')]//a[contains(@class, 'cubre-a-menuLink')]")
print("項目數量: %d" %len(list))
driver.find_element(By.XPATH, "//div[contains(@class,'is-L2open')]//a[contains(.,'卡片介紹')]").click()

cardList = driver.find_elements(By.XPATH, "//section[contains(@data-anchor-block,'blockname06')]//span[contains(@class, 'swiper-pagination-bullet')]")
for i, card in enumerate(cardList):
    card.click()
    driver.implicitly_wait(WAIT_TIME)
    driver.save_screenshot("./images/creditCard/cardScreenshot/creditCard%d.png" %(i+1))
    screenshot += 1
print("卡片數量: %d" %len(cardList))
print("總截圖數量: %d" %screenshot)

driver.quit()
