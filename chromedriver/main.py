import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from urllib.parse import unquote
from selenium.webdriver.common.keys import Keys

starturl = "https://yandex.ru/"
driver = webdriver.Chrome(executable_path=".\chromedriver.exe")


