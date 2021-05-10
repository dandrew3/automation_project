from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

contact_us_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH, "//div[13]/a")))
contact_us_btn.click()

name_field = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.NAME, "Name")))
name_field.send_keys("Donald Trump")

email_field = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.NAME, "Email")))
email_field.send_keys("donald@gmail.com")

phone_field = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.NAME, "Phone")))
phone_field.send_keys("+1987654321")

country_field = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.NAME, "Country")))
country_field.send_keys("USA")

send_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form93275870']/div[2]/div[6]/button")))
send_btn.click()

close_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH, "//div[@id='rec93275870']/div/div/div")))
close_btn.click()

home_page_btn = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//div[@data-elem-id='1551634462374']/a")))

driver.quit()