import requests

# Configure the proxy
proxies = {
    "http://": "http://@rp.proxyscrape.com:6060",
    "https://": "http://@rp.proxyscrape.com:6060"
}

url = 'http://httpbin.org/ip'

if __name__ == '__main__':
    try:
        response = requests.get(url=url, proxies=proxies)

        print('Status Code:', response.status_code)
        print('Response JSON:', response.json())
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
