import time

from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from apiGetToken import login

# 自动化浏览器driver启动
driver_path = "D:/Python27/MicrosoftWebDriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)
driver.implicitly_wait(8)

# 获取临时邮箱
url = "https://mail.cx/zh/"
driver.get(url)
get_email = driver.find_element(By.CSS_SELECTOR, "[type='text']").get_attribute("value")
print(get_email)

# 注册账号
js = 'window.open("https://dashboard.distribute.ai/auth/signup")'
driver.execute_script(js)
driver.switch_to.window(driver.window_handles[1])

email_field = driver.find_element(By.XPATH, "//div//input[@placeholder='Enter your email']")
email_field.send_keys(get_email)

password_field = driver.find_element(By.CSS_SELECTOR, "[type='password']")
password_field.send_keys("admin123")

submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

# 进入邮箱点击激活账号

driver.switch_to.window(driver.window_handles[0])
time.sleep(100)

check_email = driver.find_element(By.CSS_SELECTOR, "div.inbox_subject__XVTwf")
driver.execute_script("arguments[0].scrollIntoView(true);", check_email)
check_email.click()

verify_link = driver.find_element(By.CSS_SELECTOR, "a.button[href*='dashboard.distribute.ai']")
link_url = verify_link.get_attribute("href")
verify_link.click()



# 接口获取token
get_token = login(get_email)


driver.quit()

