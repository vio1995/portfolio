import os
import requests

def verificar_recaptcha(token):
    secret_key = os.environ.get('RECAPTCHA_SECRET_KEY')
    payload = {'secret': secret_key, 'response': token}
    
    try:
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        response_json = response.json()
        return response_json.get('success', False)
    except Exception as e:
        print(f"Erro ao verificar reCAPTCHA: {e}")
        return False