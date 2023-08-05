import requests,json,random

def random_():
    number =''
    for i in range(16):
        digit = str(random.randint(0, 9))
        number += digit
    return number


cookies = {
    '__cf_bm': '57qASwiwQlnhP0Za.0vK7m0RdQti6U0y2sVrd8xhCuw-1691244968-0-AXKdpFi4WBzX6QP+arLuCnjATvDyhhIBNRAO3kFfGwkClkGMaI21LuDKr9SfLzYtOV82WV3rhvdMhFYHYj+nlYk=',
    '_cfuvid': 'XRNFWql.81ga7z2jebYAyb9F61DUWQvtyn9Nszwixv8-1691244968772-0-604800000',
    'cf_clearance': 'KgbfW9GcvasD3NfFfhvHAFLtIyi3SvgIzA.QT3BUif0-1691245003-0-1-8137e35f.e05bb48d.b7d0e1d3-0.2.1691245003',
}

headers = {
    'authority': 'beta.theb.ai',
    'accept': 'text/event-stream',
    'accept-language': 'en-IN,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMzMWYyZWZkLWUwYjMtNDIwZi1iZjE5LWI0NDhmNDUxOTA5ZCIsImlhdCI6MTY5MTI0NTIyMywiZXhwIjoxNjkxNTA0NDIzLCJhY3Rpb24iOiJhdXRoIiwiaXNzIjoidGhlYi5haSJ9.z-TOhW8JyeiUmEKfmcOGzO9D4h1lxmrx3tJnxeNWHq0',
    'cache-control': 'no-cache',
    'origin': 'https://beta.theb.ai',
    'pragma': 'no-cache',
    'referer': 'https://beta.theb.ai/home',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-M135FU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
def gpt (text):
    fool = f'0.{random_()}'
    params = {
    'org_id': 'edaf39b4-7ef1-4a37-91ae-f870bf5b0a02',
    'req_rand':fool,
    }
    json_data = {
    'text':text,
    'category': '5be3c43f8bc740b792cce30cebdd861c',
    'model': '12cf0aaece3f4c27846aeb9c852dc0f9',
    'model_params': {
        'long_term_memory': 'auto',
    },
    'topic_id': None
    }
    response = requests.post('https://beta.theb.ai/api/conversation', params=params, cookies=cookies, headers=headers, json=json_data)
    resp = json.loads(response.text.splitlines()[-5].split(':',1)[-1])
    return (resp['content'])
