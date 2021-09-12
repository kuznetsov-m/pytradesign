from pytradesign import PyTradeSign

token = 'your_trade_model_token'

api = PyTradeSign()

print(api.trade_model_info(token))
# {'market': 'MOEX', 'name': 'test_model', 'ticker': 'SBER'}

print(api.trade_model_signals(token))
# [{'id': 'f857272d-f20b-433f-8f25-c7e03666cb37', 'is_buy': False, 'price': 308.08, 'release_datetime': '2021-07-05 10:00:00+03:00', 'signal_datetime': '2021-07-02 23:46:00+03:00', 'value': 0.0}, {'id': 'be356573-7933-47e9-8682-aa04111a930b', 'is_buy': True, 'price': 300.08, 'release_datetime': '2021-07-15 10:08:00+03:00', 'signal_datetime': '2021-07-03 01:06:54+03:00', 'value': 0.0}]

print(api.add_order(token, True, 100, 1))
# None