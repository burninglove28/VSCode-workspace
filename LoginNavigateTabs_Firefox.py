import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.firefox.options import Options

# Set up the driver
driver = None
if driver not in globals() or driver is None:
    options = Options()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0')
    service = FirefoxService(executable_path=f"./131/geckodriver.exe")
    driver = FirefoxDriver(service=service, options=options)

# SSO Login
driver.get("https://p.lgcns.com/front/")
time.sleep(1)
username = "77963"
password = "dlgywjd0102!"
driver.find_element(By.ID, "id").send_keys(username)
driver.find_element(By.ID, "pw").send_keys(password)
driver.find_element(By.ID, "btnLogin").click()
time.sleep(1)

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

# Find the button element and click it
submit_button = driver.find_element(By.CLASS_NAME, "Question_send__3ptzb")
submit_button.click()
time.sleep(3)

# Find all elements with the class name "Answer_text-wrap__FAK0g"
answer_elements = driver.find_elements(By.CLASS_NAME, "Answer_text-wrap__FAK0g")

# Get the last answer element
last_answer_element = None
if answer_elements:
    last_answer_element = answer_elements[-1]
else:
    print("No answer elements found.")

# Extract text from <p> tags within the last answer element
if last_answer_element:
    p_tags = last_answer_element.find_elements(By.TAG_NAME, "p")
    for p in p_tags:
        print(p.text)
else:
    print("No last answer element to extract text from.")
