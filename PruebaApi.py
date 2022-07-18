import requests
import json

#Variable string con la url de api
urlFinneg = 'https://api.teamplace.finneg.com/api/reports/COMPOSICIONSALDOSCLIENTES?ACCESS_TOKEN=966d9fc9-8002-4dd9-a492-445773a08012&PARAMWEBREPORT_fecha=2022-07-15&PARAMWEBREPORT_organizacion=35&PARAMWEBREPORT_circuitocontable=&PARAMWEBREPORT_cuenta=&PARAMWEBREPORT_moneda=&PARAMWEBREPORT_Empresa='

#Comprobamos la respuesta de la API
info = requests.get(urlFinneg)

if info.status_code == 200:
    print("Ahora siii pa!!")

#Leemos la infomracion de la API con el metodo '.json' de mi variable 
data = info.json()
print(type(data)) #el tipo de json (es una lista)
#print(data) #imprimimos toda la info junto

#aca tratamos de imprimir un dato del primer valor del json (que es una lista)
primer = data[0]
print(primer['COMPROBANTE'])


for i in data:
    print(i['COMPROBANTE'])


