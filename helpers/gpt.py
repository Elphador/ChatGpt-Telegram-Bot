import json ,requests

def gpt(text):
    try :
        headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-M135FU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'Referer': 'https://chatbot.theb.ai/#/chat/1002',
        }
        json_data = {
        'prompt': msg.text,
        'options': {},
        }
        
        response =  requests.post('https://chatbot.theb.ai/api/chat-process', headers=headers, json=json_data)
        resp = (json.loads(response.text.splitlines()[-1])["text"])
        return resp 
    except Exception as e :
        return e

      
      