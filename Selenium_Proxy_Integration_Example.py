import re

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Proxy server credentials and host information
proxy_address = "rp.proxyscrape.com:6060"
proxy_username = "apvx45n24g1q810"
proxy_password = "xfii55ig559jfw0"

# Selenium Wire proxy configuration
sw_options = {
    'proxy': {
        # 'http': f'http://156.228.179.167:3128',
        'http': f'http://{proxy_username}:{proxy_password}@{proxy_address}',
        # 'https': f'http://156.228.179.167:3128',
        'https': f'https://{proxy_username}:{proxy_password}@{proxy_address}',
    }
}

# Set up Chrome options (optional settings)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start Chrome maximized
chrome_options.add_argument("--disable-gpu")      # Disable GPU for compatibility
chrome_options.add_argument("--no-sandbox")       # Avoid sandboxing (useful in restricted environments)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues

# Set up WebDriver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, seleniumwire_options=sw_options, options=chrome_options)

# Access target website
driver.get('https://ssl-judge2.api.proxyscrape.com/')

# Close the browser

# Example: Extract the IP from the response
response = driver.page_source

# using simple regex to parse origin ip
your_ip: str = re.search("HTTP_X_FORWARDED_FOR = (\d+\.)+\d+", response)
print("Response:", response)
print("Your IP is:", re.search("HTTP_X_FORWARDED_FOR = (\d+\.)+\d+", response).group().split("=")[-1])

driver.quit()


