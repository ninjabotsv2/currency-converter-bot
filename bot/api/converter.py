import os

import requests

SERVER_URL = 'http://apilayer.net/api/'
API_KEY = os.environ.get('API_KEY')


class Converter:
    def convert(self, currency_from, currency_to, amount=1):
        rate = self._send_convert_request(currency_from, currency_to)

        result = rate * amount
        return result

    def _send_convert_request(self, currency_from, currency_to):
        convert_url = f'{SERVER_URL}/live'

        response = requests.get(
            url=convert_url,
            params=dict(access_key=API_KEY)
        )

        return self._get_conversion_result(response, currency_from, currency_to)

    def _get_conversion_result(self, response, currency_from, currency_to):
        if not response.json():
            raise Exception('No JSON in convert response')

        data = response.json()

        if 'quotes' in data:
            from_key = f"usd{currency_from}".upper()
            to_key = f"usd{currency_to}".upper()

            if from_key in data['quotes'] and to_key in data['quotes']:
                from_rate = data['quotes'][from_key]
                to_rate = data['quotes'][to_key]

                return to_rate / from_rate
