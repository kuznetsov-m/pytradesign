from datetime import datetime
# import pytz
import os
import json
import requests

class PyTradeSign:
    __base_url = 'https://tradesign.herokuapp.com'

    def __init__(self):
        pass

    def trade_model_info(self, trade_model_token: str) -> dict:
        url = self.__base_url + '/trade_model_info'
        headers = {'Content-Type': 'application/json'}
        body = {'model_token': trade_model_token}

        req = requests.post(url, headers=headers, data=json.dumps(body))
        
        try:
            return json.loads(req.text)
        except Exception:
            raise ValueError(f'Write signal error. Status: {req.status_code}. Text: {req.text}')

    def trade_model_signals(self, trade_model_token: str, limit: int = 100, offset: int = 0) -> dict:
        url = self.__base_url + f'/api/trade_model/{trade_model_token}/signals?limit={limit}&offset={offset}'
        headers = {'Content-Type': 'application/json'}

        req = requests.get(url, headers=headers)
        
        try:
            return json.loads(req.text)
        except Exception:
            raise ValueError(f'Get trade model signals error. Status: {req.status_code}. Text: {req.text}')

    def add_order(
        self,
        trade_model_token: str,
        is_buy: bool,
        price: float,
        value: float
    ):
        url = self.__base_url + f'/api/trade_model/{trade_model_token}/add_order'
        
        headers = {'Content-Type': 'application/json'}
        body = {
            'price': price,
            'is_buy': is_buy,
            'value': value
        }

        req = requests.post(url, headers=headers, data=json.dumps(body))
        
        if req.text != 'ok':
            raise ValueError(f'Write signal error. Status: {req.status_code}. Text: {req.text}')