import os

import requests

SERVER_URL = 'https://free.currconv.com/api/v7'
API_KEY = os.environ.get('API_KEY')


class Converter:
    def __init__(self):
        self._currencies_query = None

    def convert(self, currency_from, currency_to, amount=1):
        self._currencies_query = f"{currency_from}_{currency_to}".upper()
        rate = self._send_convert_request()

        result = rate * amount
        return result

    def _send_convert_request(self):
        convert_url = f'{SERVER_URL}/convert'

        response = requests.get(
            url=convert_url,
            params=dict(
                q=self._currencies_query,
                apiKey=API_KEY
            )
        )

        return self._get_conversion_result(response)

    def _get_conversion_result(self, response):
        if not response.json():
            raise Exception('No JSON in convert response')

        data = response.json()
        if 'results' in data:
            if self._currencies_query in data['results']:
                return data['results'][self._currencies_query]['val']

