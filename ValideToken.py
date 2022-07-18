import requests
import json

def GeneradorToken(ClientId, ClientSecret):

    str1 = 'https://api.teamplace.finneg.com/api/oauth/token?grant_type=client_credentials&client_id='
    str2 = '&client_secret='
    
    urlOauth = str1 + ClientId + str2 + ClientSecret
    
    token = requests.get(urlOauth)

    if token.status_code == 200:
        print("TOKEN VALIDO")

    clave = token.text
    return clave


