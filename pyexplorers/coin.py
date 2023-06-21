import json
import requests


class Coin:
    """
        Generic class for a crypto coinn
    """

    def __init__(self, *, api: str, api_key: str) -> None:
        self.api = api
        self.api_key = api_key

    @property
    def symbol(self):
        return self.__class__.__name__
    
    def get(self, **kwargs):
        base_url = f"https://{self.api}?"
        for key, value in kwargs.items():
            base_url += f"{key}={value}&"
        
        base_url += f"apikey={self.api_key}"
        resp = requests.get(base_url)

        if resp.status_code == 200:
            return json.loads(resp.text)

# https://api.etherscan.io/api?module=account&action=balance&address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&tag=latest&apikey=542REPGZRRMR8CEP16KD8FM4QUKMGZ78H1