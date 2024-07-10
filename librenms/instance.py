import requests

class LibreNMSAPI:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.api_token = api_token

    def get(self, endpoint):
        url = f'{self.base_url}{endpoint}'
        headers = {
            'X-Auth-Token': self.api_token,
        }
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
