import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


try:
    # Open the webpage
    driver.get("https://likhupike-demo.palikasoft.com")

    # Scroll down the webpage
    target_y = 6000
    scroll_distance = 500
    current_y = 0
    while current_y < target_y:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance
        time.sleep(2)

    # Scroll up the webpage
    target_y_up = 0  # Target vertical scroll position for scrolling up
    scroll_distance = -500  # Negative value to scroll up
    current_y = 6000  # Assuming the current vertical scroll position is at the bottom of the page

    while current_y > target_y_up:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance  # Decrementing the current_y position
        time.sleep(2)

    # Wait for the contact element to be visible
    Contact_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()='Contact']"))
    )

    Contact_element.click()
    time.sleep(3)

finally:
    # Close the WebDriver
    driver.quit()
    print("Congrats!! Code ran successfully")