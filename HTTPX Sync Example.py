import httpx

def sync_request_with_proxy():
    proxies = {
        "http://": "http://@rp.proxyscrape.com:6060",
        "https://": "http://@rp.proxyscrape.com:6060"
    }

    with httpx.Client(proxies=proxies) as client:
        response = client.get('http://httpbin.org/ip')

        print("Status Code:", response.status_code)
        print("Response:", response.json())

if __name__ == '__main__':
    sync_request_with_proxy()
