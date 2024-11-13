from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Proxy setup
proxy_address = "rp.proxyscrape.com:6060"
proxy_username = "your_proxy_username"
proxy_password = "your_proxy_password"

# Chrome options setup
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_address}')

if proxy_username and proxy_password:
    from selenium.webdriver.common.proxy import Proxy, ProxyType

    # Create a proxy with authentication
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = proxy_address
    proxy.ssl_proxy = proxy_address

    # Add the proxy to Chrome options
    chrome_options.Proxy = proxy
    chrome_options.add_argument('--proxy-bypass-list=*')

# Initialize the driver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://httpbin.org/ip")

print(driver.page_source)

driver.quit()
