from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
# edge_options.page_load_strategy = 'eager'
medriver_path = "C:\webdrivers\msedgedriver.exe"  # causes browser mismatch
service = Service(medriver_path)
driver = webdriver.Edge(options=edge_options, service=service)
driver.get("https://www.linkedin.com/feed/")

# sign_in = driver.find_element(By.CLASS_NAME, value="nav__button-secondary btn-secondary-emphasis btn-md")
# print(sign_in)

def dialog_check():
  apply_dialog = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div")
  dialog_input = len(apply_dialog.find_elements(By.TAG_NAME, value="input"))
  if dialog_input > 1:
    return True


username = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
sign_in = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')
username.send_keys("szymonbryniak8@gmail.com")
password.send_keys("Password_12345!")
time.sleep(5)
sign_in.click()
jobs = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
jobs.click()
time.sleep(3)
#################### job search sometimes not found
try:
  job_search = driver.find_element(By.XPATH, value='/html/body/div[7]/header/div/div/div/div[2]/div[2]/div/div/input[1]')
except:
  job_search = driver.find_element(By.XPATH, value='/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')

job_search.send_keys("Python Developer")
job_search.send_keys(Keys.ENTER)

time.sleep(2)
easy_apply = driver.find_element(By.ID, value='searchFilter_applyWithLinkedin')
easy_apply.click()
time.sleep(2)

#################### EASY APPLY JOB
try:
  easy_apply_job = driver.find_element(By.XPATH, value='/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[6]/div/div/div/button')
  easy_apply_job.click()
  time.sleep(2)
except:
  print('element not found: easy apply 1 58')

try:
  easy_apply_job = driver.find_element(By.XPATH, value='/html/body/div[7]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button')
  easy_apply_job.click()
  time.sleep(2)
except:
  print('element not found: easy apply 2 65')

try:
  easy_apply_job = driver.find_element(By.XPATH, value='/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button')
  easy_apply_job.click()
  time.sleep(2)
except:
  print('elemenet not found: easy apply 3 72')
####################

def fill_in():
  #################### mobile
  try:
    mobile = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input")
    mobile.send_keys("07877611724")
    print('mobile number entered: 80')
    time.sleep(2)
  except:
    print('element not found: mobile 82')

  try:
    next = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
    next.click()
    time.sleep(2)
  except:
    print('element not found: next')

  #################### location
  try:
    location = driver.find_element(By.XPATH, value='//*[@id="single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4085306280-10291243194-location-GEO-LOCATION"]')
    location.send_keys("Greater London, England, United Kingdom")
    time.sleep(2)
  except:
    print('element not found:  location')

  #################### next 
  try:
    next = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
    next.click()
    time.sleep(2)
  except:
    print('element not found: next')
  #################### review sometimes not found

  try:
    review = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
    review.click()
    time.sleep(2)
  except:
    print('element not found: review')

  try:
    submit = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/div[2]/div/div/form/footer/div[3]/button")
    submit.click()
    time.sleep(2)
  except:
    X = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/button")
    X.click()
    time.sleep(2)

    dialog_save = driver.find_element(By.XPATH, value="/html/body/div[4]/div[2]/div/div[3]/button[2]")
    dialog_save.click()

  try:
    X = driver.find_element(By.XPATH, value="/html/body/div[4]/div/div/button")
    X.click()
    time.sleep(2)
  except:
    print('element not found: X')



fill_in()
