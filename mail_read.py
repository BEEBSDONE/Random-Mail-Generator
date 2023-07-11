from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

# Initialize driver
driver = webdriver.Firefox()  # or use another browser driver
driver.get("https://www.yopmail.com/en/");

#Accept cookies(My part KEKW)

#driver.find_element(By.ID,"necesary").click();
login_button = driver.find_element(By.ID, "necesary");
ActionChains(driver)\
    .click(login_button)\
    .perform()

#my part of code LOLZ
mail_path = os.path.join(os.path.dirname(__file__), "mail.txt");
with open(mail_path, 'r') as file:
    mail_address = file.read();
    print("mail address: "+mail_address);

# Enter the email address
login_button = driver.find_element(By.ID, "login");
ActionChains(driver)\
    .click(login_button)\
    .perform()
login_button.send_keys(mail_address);  # replace with your YOPMail email

#submit login button
login_button = driver.find_element(By.CSS_SELECTOR, ".f36");
ActionChains(driver)\
    .click(login_button)\
    .perform() 

# Wait for the email list to load in the iframe
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ifinbox")));

# Get the list of emails
email_elements = driver.find_elements(By.CSS_SELECTOR, "div.m");

email_data = [];
for email_element in email_elements:
    email_subject = email_element.find_element(By.CLASS_NAME, "lms").text;
    email_timestamp = email_element.find_element(By.CLASS_NAME, 'lmh').text;
    email_data.append((email_subject, email_timestamp));

for i, (email_subject, email_timestamp) in enumerate(email_data):
    # Get the email element again as the previous reference might be stale
    email_element = driver.find_element(By.CLASS_NAME, "lmfd");

    # Click on the email to load it in the other frame
    email_element.click();

    # Switch back to default content
    driver.switch_to.default_content();

    # Wait for the email content to load in the other frame
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "ifmail")));

    # Get the content of the email
    content = driver.find_element(By.CSS_SELECTOR, 'div[dir="ltr"]').text;

    print(f"Email {i+1}:");
    print(f"Subject: {email_subject}");
    print(f"Timestamp: {email_timestamp}");
    print(f"Content: {content}");
    print("");

    # Switch back to the email list frame for the next iteration
    driver.switch_to.default_content();
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "ifinbox")));

# Close the browser
driver.quit();
