from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os

geckodriver = os.environ['geckodriver'] 
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
browser.get('http://localhost:8000')

assert 'Django' in browser.title