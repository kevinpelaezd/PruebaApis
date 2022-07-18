import requests
import json

def GeneradorToken():

    urlOauth = 'https://api.teamplace.finneg.com/api/oauth/token?grant_type=client_credentials&client_id=0d7eb792c49726e7d48ca2d69e5f08ca&client_secret=aa8916e0da6075e94356055615eade38'

    token = requests.get(urlOauth)

    if token.status_code == 200:
        print("TOKEN VALIDO")

    clave = token.text
    return clave

key = GeneradorToken()

print(key)
print(type(key))

parte1 = 'https://api.teamplace.finneg.com/api/reports/stockDeposito?ACCESS_TOKEN=' 
parte2=  '&PARAMWEBREPORT_fecha=2022-07-15&PARAMWEBREPORT_ConceptoID=&PARAMWEBREPORT_producto=&PARAMWEBREPORT_deposito=&PARAMWEBREPORT_organizacion=&PARAMWEBREPORT_numeroPartida=&PARAMWEBREPORT_tipoStock=&PARAMWEBREPORT_circuitocontable=&PARAMWEBREPORT_soloStockNoCero=false&PARAMWEBREPORT_soloStockDebajoPtoReposicion=false&PARAMWEBREPORT_soloDepositos=0&PARAMWEBREPORT_Empresa=&PARAMWEBREPORT_TipoPrecio=0&PARAMWEBREPORT_AgruparPor=1&PARAMWEBREPORT_MonedaID=PES'
urlStock = parte1+key+parte2


print(urlStock)

flag = requests.get(urlStock)

if flag.status_code == 200:
    print("Todo OK")
else:
    print("No entro")    


