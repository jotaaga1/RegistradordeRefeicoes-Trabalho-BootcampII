import requests

API_KEY = "BDgPysYzp8cgJdph2P55dfZ1jOrWHuszazb67Wj6"

def buscar_alimento(nome):
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"

    params = {
        "query": nome,
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)

    return response.json()