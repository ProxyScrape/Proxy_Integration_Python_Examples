from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define the proxy details
proxy = "156.228.179.167:3128"

# Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up proxy
chrome_options.add_argument(f'--proxy-server=http://{proxy}')

# Set up the WebDriver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Test the proxy by visiting a website
driver.get("http://httpbin.org/ip")  # This site shows the IP address used for the request

# Print the page source to check the proxy IP
print(driver.page_source)
if __name__ == '__main__':

    driver.quit()