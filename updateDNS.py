from typing import Tuple
import requests
import optparse
from optparse_mooi import CompactHelpFormatter

from DNSChanger import DNSChanger
from DNSRecord import DNSRecord

def get_current_ip() -> str:
    response = requests.get("https://ipinfo.io/json", verify=True)
    return response.json()["ip"]

def options() -> Tuple:
    parser = optparse.OptionParser(formatter=CompactHelpFormatter())
    parser.add_option(
        "-k", "--key",
        action="store", dest="api_key", 
        type=str, 
        help="Your Gandi API Key"
    )
    parser.add_option(
        "-d", "--domain",
        action="store", dest="domain",
        type=str, 
        help="Your domain you want to update"
    )
    parser.add_option(
        "-n", "--name",
        action="store", dest="name",
        type=str, default="@",
        help="Record Name. Default is '@'"
    )
    parser.add_option(
        "-t", "--type",
        action="store", dest="type",
        type=str, default="A",
        help="Record Type. Default is 'A'"
    )
    parser.add_option(
        "-l", "--ttl",
        action="store", dest="ttl",
        type=int, default=10800,
        help="Record Time to Live. Default is 10800"
    )
    options, _ = parser.parse_args()

    if options.api_key is None:
        print("ERROR: You have to specify an API key")
        exit()
    if options.domain is None:
        print("ERROR: You have to specify a domain")
        exit()

    return options

def update(name: str, type: str, values: str, ttl: int, api_key: str, domain: str) -> None:
    rec = DNSRecord(name, type, values=[values])
    dns = DNSChanger(api_key, domain, record=rec)

    response = dns.get_record()

    match response.status_code:
        case 400:
            print("Error: Invalid record type!")
        case 401:
            print("Bad authentication attempt because of a wrong API Key.")
        case 403:
            print("Access to the resource is denied. Mainly due to a lack of permissions to access it.")
        case 404:
            print("Record does not exist! Creating record...")
            r = dns.create_record()
            print(r.text)
            if r.status_code == 201:
                print("The specified record has been created successfully!")
            else:
                print(f"Error: Could not create the specified record due to an unexpected error! Status code: {r.status_code}")
        case _:
            print("Updating the specified record...")
            r = dns.update_record()
            if r.status_code == 201:
                print("The specified record has been updated successfully!")
            else:
                print(f"Error: Could not update the specified record due to an unexpected error! Status code: {r.status_code}")


if __name__ == "__main__":
    opt = options()
    my_ip = get_current_ip()
    update(name=opt.name, type=opt.type, values=my_ip, ttl=opt.ttl, api_key=opt.api_key, domain=opt.domain)