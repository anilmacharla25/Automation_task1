start_time = datetime.now()
# print(f"Login successful at: {start_time.strftime('%H:%M:%S')}")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains  # Import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import threading
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options

# Setup WebDriver in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode
chrome_options.add_argument("--window-size=1920x1080")  # Set window size (optional)
chrome_options.add_argument("--no-sandbox")
# Setup WebDriver
# service = Service(executable_path="C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(options= chrome_options)

driver.implicitly_wait(10)
# driver.set_window_size(1920,1080)
driver.maximize_window()
url = "https://secure12.oncoemr.com/nav/referrals?locationId=LH_Cz108527942_27"
driver.get(url)


Email = driver.find_element(By.XPATH, '//input[@id="Email"]')
Email.send_keys("XXXXXXXXX")

password = driver.find_element(By.XPATH, '//input[@type="password"]')
password.send_keys("XXXXXXX@1111")

login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

# start_time = datetime.now()
# print(f"Login successful at: {start_time.strftime('%H:%M:%S')}")


driver.find_element(By.XPATH, '//div[text()="American Infusion Center"]').click()
driver.find_element(By.XPATH, '//a[text()="Demographics"]').click()
driver.find_element(By.XPATH, '//a[@id="ancNewPatient"]').click()

lock = threading.Lock()


def fill_field(locator, value=None, field_type="input"):
    with lock:  
        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.ID, "modalIframeId0")))
        driver.switch_to.frame(iframe)  
        try:
            if field_type == "input":
                driver.find_element(By.XPATH, locator).send_keys(value)
            elif field_type == "select":
                dropdown = Select(driver.find_element(By.XPATH, locator))
                dropdown.select_by_visible_text(value)
            elif field_type == "click":
                try:
          
                    wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()
                except selenium.common.exceptions.ElementClickInterceptedException:
                    print(f"ElementClickInterceptedException for locator: {locator}. Trying alternate methods...")
                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
#                     time.sleep(0.5)  
                    try:
                        element.click()
                    except:
                        ActionChains(driver).move_to_element(element).click().perform()
            
        finally:
            driver.switch_to.default_content()  # Switch back to default content
def click_save_button():
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "modalIframeId0"))
        )
        driver.switch_to.frame(iframe) 
        save_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="btnBack"]'))
        )
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.2)  

        driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        time.sleep(0.2)  

        action = ActionChains(driver)
        action.move_to_element(save_button).click().perform()

        print("Save button clicked successfully.")
    except Exception as e:
        print(f"An error occurred while trying to click the Save button: {e}")
    finally:
        driver.switch_to.default_content()  


def fill_chunk1():
    fill_field('//input[@name="txtFirstName"]', "Stella")
def fill_chunk2():
    fill_field('//input[@name="txtMiddleName"]', "Singh")
def fill_chunk3():
    fill_field('//input[@name="txtLastName"]', "XYZ")
def fill_chunk4():
    fill_field('//input[@name="txtSalutation"]', "Mrs")
def fill_chunk5():
    fill_field('//input[@name="txtPreferredName"]', "ABC")
def fill_chunk6():
    fill_field('//input[@id="cldrDOB_dateInput"]', "01/01/1990")
def fill_chunk7():
    fill_field('//input[@name="txtCity"]', "New York")
def fill_chunk8():
    fill_field('//input[@id="cldrDOD_dateInput"]', "01/01/2022")
def fill_chunk9():
    fill_field('//select[@name="ddlMaritalStatus"]', "Married", field_type="select")
def fill_chunk10():
    fill_field('//select[@id="ddlStates"]', "Iowa", field_type="select")
def fill_chunk11():
    fill_field('//input[@id="yesSiblings"]', field_type="click")
def fill_chunk12():
    fill_field('//*[@id="sex-edit-row-react-mount"]/td[2]/div/div[2]/label/span', field_type="click")
def fill_chunk13():
    fill_field('//input[@id="chkIsTestPatient"]', field_type="click")
def fill_chunk14():
    fill_field('//input[@value="Hispanic or Latino"]', field_type="click")
    

# Create threads for each chunk
threads = [
    threading.Thread(target=fill_chunk1),
    threading.Thread(target=fill_chunk2),
    threading.Thread(target=fill_chunk3),
    threading.Thread(target=fill_chunk4),
    threading.Thread(target=fill_chunk5),
    threading.Thread(target=fill_chunk6),
    threading.Thread(target=fill_chunk7),
    threading.Thread(target=fill_chunk8),
    threading.Thread(target=fill_chunk9),
    threading.Thread(target=fill_chunk10),
    threading.Thread(target=fill_chunk11),
    threading.Thread(target=fill_chunk12),
    
]


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

click_save_button()
end_time= datetime.now()
print(f"End time {end_time.strftime('%H:%M:%S')}")
duration=end_time-start_time
duration_seconds = duration.total_seconds()
print(f"time duration is {duration_seconds}")

driver.quit()
