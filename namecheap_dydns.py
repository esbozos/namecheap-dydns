import requests
import sys
import getopt
import xml.etree.ElementTree as ET

url = 'https://dynamicdns.park-your-domain.com/update'


def print_usage():
    print('\n')
    print('Usage:')
    print('namecheap_dydns.py -H <host> -d <yourdomain.com> -p <yourpassword>')
    print('namecheap_dydns.py --host=<host> --domain=<yourdomain.com> --password=<yourpassword>')
    print('\n')


def get_public_ip():
    res = requests.get('https://ifconfig.me')
    ip = res.content.decode()
    return ip


def update_public_ip():
    ip = get_public_ip()


def main(argv):
    print('\n')
    host = ''
    domain = ''
    password = ''

    try:
        opts, args = getopt.getopt(
            argv, "hH:d:p:", ["host=", "domain=", "password="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    if not opts:
        print('arguments must be provided')
        print_usage()
        sys.exit(2)
    print(opts)
    for o, a in opts:
        if o == '-h':
            print_usage()
            sys.exit()

        elif o in ['-H', '-host']:
            host = a

        elif o in ['-d', '--domain']:
            domain = a

        elif o in ['-p', '--password']:
            password = a

    if not host or not domain or not password:
        print('host, domain and password are and required arguments')
        print_usage()
        sys.exit(2)

    ip = get_public_ip()
    print(f'\nYour public ip is {ip}')
    print(f'request https dynamic host update...\n')
    update_url = f'{url}?host={host}&domain={domain}&password={password}&ip={ip}'
    res = requests.get(update_url)
    try:
        root = ET.fromstring(res.content.decode('utf-8'))
        for child in root:
            print(child.tag, child.text)

    except Exception as e:
        print('error \n')
        print(e)
        sys.exit(2)

    print('\n')


if __name__ == '__main__':
    main(sys.argv[1:])
