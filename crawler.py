from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
#醫聯網登入介面
driver.get("https://sso2.med-net.com/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DK4F45Xx53bJsKyaUt7gsxJo%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fmed-net.com%252FMember%252FLoginMedNetCode%26scope%3Dopenid%2520profile%2520email")
username = driver.find_element(By.NAME, value="Username")
password = driver.find_element(By.NAME, value="Password")
username.send_keys("howard159632@gmail.com")
password.send_keys("Howard123")
loginBtn = driver.find_element(By.NAME, value="button")
loginBtn.click()
sleep(5)
