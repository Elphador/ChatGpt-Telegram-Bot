
import requests

def gpt(text):
    url = "https://freegptapi.hop.sh/neural/api"
    params = {
    "query":text}
    response = requests.get(url, params=params)
    data = response.json()
    return data['answer']
    