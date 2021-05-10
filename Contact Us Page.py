from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

contact_us_navigation_bar_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(), 'Contact Us')]")))
contact_us_navigation_bar_btn.click()

email_input_field = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.NAME, "email")))
email_input_field.send_keys("mail_test@exam.com")

submit_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form91499566']/div[2]/div[3]/button")))
submit_btn.click()

# I don't know why this doesn't work
#close_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tildaformsuccesspopup']/div/div/svg[1]/g/path[1]")))
#close_btn.click()

driver.quit()


