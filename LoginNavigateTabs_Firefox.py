import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.firefox.options import Options

# Set up the Firefox driver
options = Options()
options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0')

service = FirefoxService(executable_path=f"./131/geckodriver.exe")
driver = FirefoxDriver(service=service, options=options)

# SSO Login
driver.get("https://p.lgcns.com/front/")
time.sleep(3)
username = "77963"
password = "dlgywjd0102!"
driver.find_element(By.ID, "id").send_keys(username)
driver.find_element(By.ID, "pw").send_keys(password)
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)

# ChatEXAONE
driver.get("https://lgcns.exaone.ai/")
time.sleep(5)

# Close the modal if it appears
try:
    close_modal_button = driver.find_element(By.CLASS_NAME, "OnBoardingModal_close-icon__P7meh")
    close_modal_button.click()
except Exception as e:
    alert_script = f"alert('An exception occurred: {e}');"
    driver.execute_script(alert_script)

# Find the textarea element and input text
textarea = driver.find_element(By.CLASS_NAME, "Question_textArea__GNcnx")
textarea.send_keys("This is a test message.")
time.sleep(5)

# Find the button element and click it
submit_button = driver.find_element(By.CLASS_NAME, "Question_send__3ptzb")
submit_button.click()
