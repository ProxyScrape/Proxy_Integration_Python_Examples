import requests

def send_request_via_proxy():
    # Proxy configuration
    proxy = "http://156.228.179.167:3128"

    # Proxies dictionary for requests
    proxies = {
        "http": proxy,
        "https": proxy
    }

    # Target URL
    url = "http://httpbin.org/ip"

    try:
        # Sending a GET request via the proxy
        response = requests.get(url, proxies=proxies)

        # Checking if the response is successful
        if response.status_code == 200:
            print("Response received successfully:")
            print(response.json())
        else:
            print(f"Failed to retrieve response. HTTP Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_request_via_proxy()
