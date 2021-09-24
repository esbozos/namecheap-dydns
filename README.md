# namecheap-dydns
simple Python script to dynamically update the host's IP with an HTTP request to namecheap.com 

## Requirements:
Python3 and requests lib.

```bash
pip install requests
```

### Usage:
#### Example:
```bash
python namecheap_dydns.py -H <host> -d <domain.com> -p <password>
```

### Options:

- -h Show usage information
- -d --domain= set your FQDN (Full qualified domain name) parked in namecheap.com
- -p --password= set your Dynamic DNS Password provided from namecheap.com in Advance DNS tab.
- -H --host= set the host to be updated with your public IP address, the host record should be "A + Dynamic DNS Record" type.

### Automatization:

This script could be configured to run automatically in background to keep your DNS record updated. Namecheap client is set to run every 15 minutes as default, we can use a cronjob to reach the same approach.


```cronjob
*/15 * * * * /usr/local/bin/python3 /<PATH_TO_SRC>/namecheap-dydns/namecheap_dydns.py -H <yourhost> -d <yourdomain.com> -p <yourpassword>
```

### Credits:

This script use https://ifconfig.me service to determine your public IPv4 address.

### Expected output:

```bash
Your public ip is 186.118.90.255
request https dynamic host update...

Command SETDNSHOST
Language eng
IP 186.118.90.255
ErrCount 0
ResponseCount 0
Done true
debug None
```
