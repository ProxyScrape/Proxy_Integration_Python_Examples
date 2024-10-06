import urllib.request


if __name__ == '__main__':
    proxies = {
        "http://": "http://@rp.proxyscrape.com:6060",
        "https://": "http://@rp.proxyscrape.com:6060"
    }

    proxy_handler = urllib.request.ProxyHandler(proxies)

    opener = urllib.request.build_opener(proxy_handler)

    urllib.request.install_opener(opener)

    try:
        response = urllib.request.urlopen("http://httpbin.org/ip")
        content = response.read().decode('utf-8')
        print("Web page content:", content)
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")