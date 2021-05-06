from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://datafolks.com")

logo_Home = driver.find_element_by_xpath("(//a[contains(@href, 'https://datafolks.com/')])[2]")
assert logo_Home.text == "Home"

logo_Portfolio = driver.find_element_by_xpath("//a[contains(@href, 'https://datafolks.com/Portfolio')]")
assert logo_Portfolio.text == "Portfolio"


logo_Services = driver.find_element_by_xpath("//a[contains(@href, 'https://datafolks.com/Services')]")
assert logo_Services.text == "Services"


logo_Contact_Us = driver.find_element_by_xpath("//a[contains(@href, 'https://datafolks.com/Contacts')]")
assert logo_Contact_Us.text == "Contact Us"


driver.quit()
