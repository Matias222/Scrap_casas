from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def test_chromedriver_installation():
    # Setup Chrome options
    chrome_options = Options()
    
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # This is important for some versions of Chrome
    chrome_options.add_argument("--remote-debugging-port=9222")  # This is recommended
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")

    #chrome_options.add_argument("--headless=new")
    #chrome_options.add_argument('disable-gpu')
    #chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")


    # Set path to Chrome binary
    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    # Set path to ChromeDriver
    chrome_service = ChromeService(executable_path="/opt/chromedriver/chromedriver-linux64/chromedriver")

    # Set up driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        # URL to test
        driver.get("http://example.com")

        # Give the browser time to load all content.
        time.sleep(2)

        # Find element by tag
        element = driver.find_element(By.TAG_NAME, "h1")

        # Print the text of the element
        print(element.text)

        # Check if the text is as expected
        assert "Example Domain" in element.text
        print("ChromeDriver is installed and working as expected.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
       # Close the browser
        driver.quit()

test_chromedriver_installation()