import requests

def get_headers(domain):
    r = requests.get(domain)
    return r.headers

def get_strict_transport_security(domain):
    headers = get_headers(domain)
    try:
        return headers['Strict-Transport-Security']
    except:
        return 0

def get_x_content_type_options(domain):
    headers = get_headers(domain)
    try:
        return headers['X-Content-Type-Options']
    except:
        return 0

def get_x_xxs_protection(domain):
    headers = get_headers(domain)
    try:
        return headers['X-XXS-Protection']
    except:
        return 0

def get_referrer_policy(domain):
    headers = get_headers(domain)
    try:
        return headers['Referrer-Policy']
    except:
        return 0

def get_content_security_policy(domain):
    headers = get_headers(domain)
    try:
        return headers['Content-Security-Policy']
    except:
        return 0

def get_x_frame_options(domain):
    headers = get_headers(domain)
    try:
        return headers['X-Frame-Options']
    except:
        return 0

def get_feature_policy(domain):
    headers = get_headers(domain)
    try:
        return headers['Feature-Policy']
    except:
        return 0

def main():
    get_headers_of_domain("https://www.signicat.com")
    print(get_strict_transport_security('https://id.signicat.com'))


if __name__ == '__main__':
    main()

