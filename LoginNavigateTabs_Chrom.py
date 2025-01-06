
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

# Set up the Edge driver
service = EdgeService(EdgeChromiumDriverManager().install())
driver = EdgeDriver(service=service)

# Open the first URL and log in
driver.get("https://p.lgcns.com/front/")
# Wait for the page to load
time.sleep(5)  

# Assuming you have the login credentials
username = "77963"
password = "dlgywjd0102!"

# Find the username and password fields and enter the credentials
driver.find_element(By.ID, "id").send_keys(username)
driver.find_element(By.ID, "pw").send_keys(password)
driver.find_element(By.ID, "btnLogin").click()
# Wait for the login process to complete
time.sleep(5) 

# Open a new tab and navigate to the second URL
driver.execute_script("window.open('https://lgcns.exaone.ai/', '_blank');")
# Wait for the new tab to load
time.sleep(5)  

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Perform any additional actions on the new tab if needed
# Close the first tab
# driver.switch_to.window(driver.window_handles[0])
# driver.close()

# Switch back to the second tab
# driver.switch_to.window(driver.window_handles[0])

# Close the modal if it appears
try:
    #close_modal_button = driver.find_element(By.CSS_SELECTOR, "OnBoardingModal_close-icon__P7meh")
    close_modal_button = driver.find_element(By.XPATH, "//button[starts-with(@class, 'OnBoardingModal')]")
    time.sleep(5)

    driver.findElement(By.cssSelector(".show")).click();
    close_modal_button.click()
except Exception as e:
    alert_script = f"alert('An exception occurred: {e}');"
    driver.execute_script(alert_script)
    time.sleep(10)  

