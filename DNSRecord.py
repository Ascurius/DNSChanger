import logging as log

class DNSRecord:

    def __init__(self, name: str, type: str, values: list, ttl: int = None):
        self.__name = name
        self.__type = type
        self.__values = values

        if ttl is None:
            self.__ttl = 10800
        else:
            self.__ttl = ttl

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def values(self):
        return self.__values

    @property
    def ttl(self):
        return self.__ttl