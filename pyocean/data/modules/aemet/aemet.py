import os
import yaml

basepath = os.path.dirname(__file__)
cfg_file=os.path.abspath(os.path.join(basepath,"aemet.yml"))
config = yaml.safe_load(open(cfg_file))

def list_codes():
    return config['codes']

def get_hourly_forecast(code):
    import requests as rq

    api_key = config['api_key']
    prod = config['products']
    headers = {'cache-control': "no-cache"}
    url = "/".join([prod['url'], prod['cities']['source'],'horaria',code])
    params = {"api_key":api_key}

    response = rq.get(url, headers=headers, params=params, verify=False)

    if response.status_code == 200:
        response = response.json()
        if response['estado'] == 200:
            data_url = response['datos']
            data = rq.get(data_url, verify=False).json()[0]

            return data["prediccion"]["dia"]

    return None
