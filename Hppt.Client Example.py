import http.client

def make_request_via_proxy():
    proxy_host = 'Proxy IP'
    proxy_port = 3128

    conn = http.client.HTTPConnection(proxy_host, proxy_port)

    target_url = 'http://httpbin.org/ip'

    conn.request("GET", target_url)

    response = conn.getresponse()
    print(f'Status: {response.status} {response.reason}')
    print(f'Body: {response.read().decode()}')

    conn.close()

if __name__ == '__main__':
    make_request_via_proxy()
