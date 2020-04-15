import requests

URI = "https://securityheaders.io/?q="

q = "https%3A%2F%2Fscotthelme.co.uk&followRedirects=on"


r = requests.get(URI+q)
r.status_code
with open("headers.txt", "a+") as f:
    f.write(str(r.headers['X-Score']))
    f.write(str(r.headers['X-Grade']))
