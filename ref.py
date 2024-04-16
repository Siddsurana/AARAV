from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webbrowser

# Provide the path to your ChromeDriver executable
#chrome_driver_path = "chromedriver.exe"

# Define Chrome options
#chrome_options = webdriver.ChromeOptions()

# Initialize Chrome WebDriver with options
#driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

# Open Google Forms
#driver.get("https://docs.google.com/forms/")

# Wait for the page to load
#time.sleep(2)
webbrowser.open("https://docs.google.com/forms/")
# Fill in the form (replace with your form field names and values)
name_field = driver.find_element_by_xpath("//input[@aria-label='Name']")
name_field.send_keys("John Doe")

email_field = driver.find_element_by_xpath("//input[@aria-label='Email']")
email_field.send_keys("johndoe@example.com")

feedback_field = driver.find_element_by_xpath("//textarea[@aria-label='Feedback']")
feedback_field.send_keys("This is a test feedback.")

# Submit the form
submit_button = driver.find_element_by_xpath("//div[@role='button' and text()='Submit']")
submit_button.click()

# Wait for submission (you may need to adjust the time depending on your form's submission speed)
time.sleep(5)

# Close the browser
driver.quit()

print("Form submitted successfully.")
