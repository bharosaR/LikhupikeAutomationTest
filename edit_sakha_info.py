import re
import time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Function to check if a string is a valid email address
def is_valid_email(email):
    try:
        # Check email format using regular expression
        email_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_pattern, email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

# Initialize Chrome WebDriver
chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open the webpage
driver.get("https://likhupike-demo.palikasoft.com")
time.sleep(1)

try:
    # Scroll down the webpage
    target_y = 6000
    scroll_distance = 500
    current_y = 0

    while current_y < target_y:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance
        time.sleep(1)

    # Scroll up the webpage
    target_y_up = 0  # Target vertical scroll position for scrolling up
    scroll_distance = -500  # Negative value to scroll up
    current_y = 6000  # Assuming the current vertical scroll position is at the bottom of the page

    while current_y > target_y_up:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance  # Decrementing the current_y position
        time.sleep(1)


    # Navigate to the login page
    login = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='login']"))
    )
    login.click()
    time.sleep(1)

    # Explicitly wait for the email field to be clickable
    email_field = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='email']"))
    )

    # Explicitly wait for the password field to be present
    password_field = WebDriverWait(driver, 2).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id=':r1:']"))
    )

    # Set values for email and password
    email = "superadmin@gmail.com"
    password = "Softech@123"

    # Enter email and password values
    email_field.clear()
    email_field.send_keys(email)
    password_field.clear()
    password_field.send_keys(password)

    # Check if the email and password fields are empty
    if not email_field:
        print("Email field cannot be empty")
    if not password_field:
        print("Password field cannot be empty")

    # Add a sleep to see the result
    time.sleep(1)

    # Check if the email address is valid
    if is_valid_email(email):
        print("Valid email address")
    else:
        print("Invalid email address")
    time.sleep(1)

    # Click the SignIn button
    sign_in_button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']"))
    )
    sign_in_button.click()
    time.sleep(1)

    target_y = 6000
    scroll_distance = 500
    current_y = 0

    while current_y < target_y:
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        current_y += scroll_distance
        time.sleep(1)

    # Navigate to आधारभूत सेटअप
    AS_field = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='__next']//ul[2]//div[1]//div[2]//span[1]"))
    )
    AS_field.click()
    time.sleep(1)

    # Navigate to कार्यालय सेटअप
    # Find the option element
    KS_field = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(@class,'MuiPaper-root MuiPaper-elevation MuiPaper-elevation0 MuiDrawer-paper MuiDrawer-paperAnchorLeft MuiDrawer-paperAnchorDockedLeft css-1l8j5k8')]//p[contains(@class,'MuiTypography-root MuiTypography-body1 css-9l3uo3')][contains(text(),'कार्यालय सेटअप')]"))
    )
    KS_field.click()
    time.sleep(1)

    # Navigate to शाखा
    शाखा = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable(
        (By.XPATH, '//div[@id="__next"]//div[contains(@class,"MuiCollapse-entered css-c4sutr")]//div[3]//div[2]'))
    )
    शाखा.click()
    time.sleep(1)

    def find_and_click(driver, xpath, timeout=2):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            print(f"Clicked on element with XPath: {xpath}")
            return element
        except TimeoutException:
            print(f"Timeout: Element with XPath {xpath} was not clickable within {timeout} seconds")
        except NoSuchElementException:
            print(f"Error: Element with XPath {xpath} not found")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    def find_element(driver, xpath, timeout=2):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            print(f"Found element with XPath: {xpath}")
            return element
        except TimeoutException:
            print(f"Timeout: Element with XPath {xpath} was not found within {timeout} seconds")
        except NoSuchElementException:
            print(f"Error: Element with XPath {xpath} not found")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None


        # Navigate to the edit page if necessary
        edit_button_2 = "//tbody/tr[2]/td[3]/div[1]//*[name()='svg']"
        find_and_click(driver, edit_button_2)
        time.sleep(1)

    try:
        # Locate the input fields
        nepali_field_xpath = find_element(driver, "//input[@placeholder='शाखाको नाम(नेपाली)']")
        english_field_xpath = find_element(driver,"//input[@name='nameEng']")
        code_field_xpath = find_element(driver, "//input[@placeholder='कोड']")

        nepali_field = find_element(driver, nepali_field_xpath)
        english_field = find_element(driver, english_field_xpath)
        code_field = find_element(driver, code_field_xpath)

        # Set values for the fields
        Sakha_name_nepali = "कोटेश्वोर"
        Sakha_name_english = "Koteshwor"
        code = "3"

        # Clear and enter new values in the respective fields
        if nepali_field:
            nepali_field.clear()
            nepali_field.send_keys(Sakha_name_nepali)
            print("Entered value in शाखाको नाम(नेपाली)")

        if english_field:
            english_field.clear()
            english_field.send_keys(Sakha_name_english)
            print("Entered value in शाखाको नाम(English)")

        if code_field:
            code_field.clear()
            code_field.send_keys(code)
            print("Entered value in कोड")

        time.sleep(1)

        # Click the Submit button to save changes
        submit_button_xpath = "//button[@type='submit']"
        find_and_click(driver, submit_button_xpath)
        time.sleep(1)

    except Exception as e:
            print(f"An error occurred during script execution: {e}")

finally:
    try:
        driver.quit()
    except Exception as e:
        print(f"Error while closing the browser: {e}")