from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

worth_it_btn = WebDriverWait(driver, 20) .until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#short']/u")))
worth_it_btn.click()


areas_of_expertise = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Areas of expertise')]")))

mobile_development_img = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src, 'icons8-smartphone-ta.svg')]")))
mobile_development_text = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Mobile Development')]")))

web_development_img = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src, 'icons8-console_1.svg')]")))
web_development_text = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Web Development')]")))

augmented_reality_img = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src, 'icons8-3d-model.svg')]")))
augmented_reality_text = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Augmented Reality')]")))

virtual_reality_img = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src, 'icons8-3ds-max.svg')]")))
virtual_reality_text = WebDriverWait(driver, 20) .until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Virtual Reality')]")))


driver.quit()