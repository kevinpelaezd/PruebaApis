import requests
import json
from ValideToken import *
import pandas as pd
from pandas import json_normalize

Token = GeneradorToken('a843eb5642cbc99fed7af5d62fc1c764','176acd327ffd43fd858680d4a7efc475')

str1 = 'https://api.teamplace.finneg.com/api/reports/stockDeposito?ACCESS_TOKEN='
str2 = '&PARAMWEBREPORT_fecha=2022-07-18&PARAMWEBREPORT_ConceptoID=&PARAMWEBREPORT_producto=&PARAMWEBREPORT_deposito=&PARAMWEBREPORT_organizacion=&PARAMWEBREPORT_numeroPartida=&PARAMWEBREPORT_tipoStock=&PARAMWEBREPORT_circuitocontable=&PARAMWEBREPORT_soloStockNoCero=false&PARAMWEBREPORT_soloStockDebajoPtoReposicion=false&PARAMWEBREPORT_soloDepositos=0&PARAMWEBREPORT_Empresa=&PARAMWEBREPORT_TipoPrecio=0&PARAMWEBREPORT_AgruparPor=1&PARAMWEBREPORT_MonedaID=PES'

urlStock = str1+Token+str2

#print(urlStock)

informacion = requests.get(urlStock)

if informacion.status_code == 200:
    print("Ahora siii pa!!")
else:
    print("No entro!")
    
    
#ESTA ES LA CLAVEEEE. Convertir la respuesta de la api en Json. para poder recorrerlo. 
#data = informacion.json()

#ESTAS DOS LINEAS SON LAS QUE GENERAN UN EXCEL. 
df = json_normalize(informacion.json())
df.to_excel('Archivo1.xlsx')
