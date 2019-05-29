import os

import requests

SERVER_URL = 'http://apilayer.net/api/'
API_KEY = os.environ.get('API_KEY')


class Converter:
    def convert(self, currency_from, currency_to, amount=1):
        rate = self._send_convert_request(currency_from, currency_to, amount)

        result = rate * amount
        return result

    def _send_convert_request(self, currency_from, currency_to, amount):
        convert_url = f'{SERVER_URL}/live'

        response = requests.get(
            url=convert_url,
            params={
                'source': currency_from,
                'access_key': API_KEY
            }
        )

        return self._get_conversion_result(response, currency_from, currency_to)

    def _get_conversion_result(self, response, currency_from, currency_to):
        if not response.json():
            raise Exception('No JSON in convert response')

        data = response.json()
        if 'quotes' in data:
            key = f"{currency_from}{currency_to}".upper()
            if key in data['quotes']:
                return data['quotes'][key]
