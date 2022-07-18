import requests

def RenovarToken (ClientId, SecretKey, bToken):


    primera = 'https://api.teamplace.finneg.com/api/oauth/token?grant_type=refresh_token&client_id='
    segunda = '&client_secret='
    tercera = '&refresh_token='

    urlOuth = primera+ClientId+segunda+SecretKey+tercera+bToken

   # print(urlOuth)

    url = requests.get(urlOuth)

    if url.status_code == 200 :
        print("Se renovo el token\n")
        return bToken
    else:
        print("No se renovo el token \n")
        return -1

