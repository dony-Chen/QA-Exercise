from appium import webdriver


capabilities = { 'browserName': 'Chrome', 'automationName': 'UIAutomator2', 'platformName': 'Android', 'platformVersion': '5.1' }
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

i = 1
driver.get('https://www.cathaybk.com.tw/cathaybk/')
#driver.save_screenshot('login.png')
driver.save_screenshot('./images/login/login.png')
#driver.save_screenshot('login.png')
driver.implicitly_wait(5)
i += 1
driver.find_element_by_class_name('cubre-o-header__burger').click()
#driver.find_element_by_css_selector(.cubre-o-nav__menu .cubre-o-menu__item:nth-child(1)).click()
driver.find_element_by_xpath('//div[3]/div/div[2]/div/div/div/div/div').click()
#driver.find_element_by_class_name('cubre-o-menu__item:nth-child(1)').click().click()
#driver.find_element_by_class_name('cubre-o-menu__btn').click()
#driver.find_element_by_class_name('cubre-a-menuSortBtn').click()
#div = driver.find_element_by_id('i_am_an_id')


#driver.find_element_by_id('comments').send_keys('My comment')


driver.quit()
