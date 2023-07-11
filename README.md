# Random Mail Generator

This repo uses Selenium to create and recover the mails.

pip install selenium

You need to download Selenium and the driver that goes with your browser.

For example if you are using Chome, you need to download ChromeDriver,
or if you are using firefox, you need to install geckodriver to control the browser.

GENERATION AND READER SCRIPT IS USING FIREFOX BY DEFAULT.

IF YOU ARE USING CHROME, DON'T FORGET TO CHANGE ON BOTH SCRIPTS:

driver = webdriver.Firefox(); 

TO:

driver = webdriver.Chrome();

PLACE BOTH OF SCRIPTS ON THE SAME PATH BEFORE LAUNCHING ANY OF THEM.
