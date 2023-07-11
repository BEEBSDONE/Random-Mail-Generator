from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#Settings
website = 'https://yopmail.com/email-generator';
driver = webdriver.Firefox();
driver.get(website);

#Elements
mail_id = driver.find_element("id","geny");
mail = mail_id.text;
username = driver.find_element("xpath", "/html/body/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div/span[1]");
iframe = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')));
driver.switch_to.frame(iframe);
select_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'seldom')));
select = Select(select_element);
options = select.options;
altdomain = options[0].text;
driver.switch_to.default_content();

#Write a file with the mail for future use
mailfile = open("mail.txt", 'w');
mailfile.write(mail);
mailfile.close

#Output
print("Outgoing Mail: "+username.text+altdomain);
print("Reception Mail: "+mail);
driver.close();
