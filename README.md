# DNSChanger

This tool is used for updating the 'A' or 'AAAA' DNS records of your domain at Gandi.net and set them to your current public IPv4/IPv6 adress

### Available Options

```bash
updateDNS.py -h
Usage: updateDNS.py [options]

 -h, --help             show this help message and exit
 -k, --key <api_key>    Your Gandi API Key
 -d, --domain <domain>  Your domain you want to update
 -n, --name <name>      Record Name. Default is '@'
 -t, --type <type>      Record Type. Default is 'A'
 -l, --ttl <ttl>        Record Time to Live. Default is 10800
 ```
 
 If you would like to add any functionalities, please add a pull request.
