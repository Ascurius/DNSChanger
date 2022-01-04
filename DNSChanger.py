import json
import requests
from DNSRecord import DNSRecord


class DNSChanger:

    BASE_URL = "https://api.gandi.net/v5/livedns/domains"

    def __init__(self, api_key: str, domain: str, record: DNSRecord):
        self.__api_key = api_key
        self.domain = domain
        self.record = record

    def get_all_records(self) -> requests.Response:
        url = f"{self.BASE_URL}/{self.domain}/records"
        header = {"Authorization": f"Apikey {self.__api_key}"}
        response = requests.get(url, headers=header)
        return response

    def get_record(self) -> requests.Response:
        url = f"{self.BASE_URL}/{self.domain}/records/{self.record.name}/{self.record.type}"
        header = {"Authorization": f"Apikey {self.__api_key}"}
        response = requests.get(url, headers=header)
        return response

    def update_record(self) -> requests.Response:
        url = f"{self.BASE_URL}/{self.domain}/records/{self.record.name}/{self.record.type}"
        header = {"Authorization": f"Apikey {self.__api_key}"}
        body = self.__generate_body(True)
        response = requests.put(url, headers=header, data=body)
        return response

    def remove_records(self) -> requests.Response:
        url = f"{self.BASE_URL}/{self.domain}/records/{self.record.name}/{self.record.type}"
        header = {"Authorization": f"Apikey {self.__api_key}"}
        response = requests.delete(url, headers=header)
        return response

    def create_record(self) -> requests.Response:
        url = f"{self.BASE_URL}/{self.domain}/records"
        header = {
            "Authorization": f"Apikey {self.__api_key}",
            "Accept": "application/json"
        }
        body = self.__generate_body(False)
        response = requests.post(url, headers=header, data=body)
        return response

    def __generate_body(self, update: bool) -> str:
        if update:
            body = {"rrset_values": self.record.values}
        else:
            body = {
                "rrset_name": self.record.name,
                "rrset_type": self.record.type,
                "rrset_values": self.record.values,
                "rrset_ttl": self.record.ttl
            }
        return json.dumps(body, indent=4)