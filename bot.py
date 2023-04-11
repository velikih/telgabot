import json
import requests
from config import keys
class APIException(Exception):
    pass
class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if == == base:
            raise APIException(f'Невозможно перевести в одну валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неизвестная валюта {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неизвестная валюта {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise

        r
        total_base
        return