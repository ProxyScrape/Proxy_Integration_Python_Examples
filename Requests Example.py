import requests

# Configure the proxy
proxies = {
    "http://": "http://156.228.179.167:3128",
    "https://": "http://156.228.179.167:3128"
}

url = 'http://httpbin.org/ip'

if __name__ == '__main__':
    try:
        response = requests.get(url=url, proxies=proxies)

        print('Status Code:', response.status_code)
        print('Response JSON:', response.json())
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
