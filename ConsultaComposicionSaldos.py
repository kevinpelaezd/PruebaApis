import requests
import json
import pandas as pd
from pandas import json_normalize
from ValideToken import *

Token = GeneradorToken('a843eb5642cbc99fed7af5d62fc1c764','176acd327ffd43fd858680d4a7efc475')


primera = 'https://api.teamplace.finneg.com/api/reports/COMPOSICIONSALDOSCLIENTES?ACCESS_TOKEN='
segunda = '&PARAMWEBREPORT_fecha=2022-07-18&PARAMWEBREPORT_organizacion=&PARAMWEBREPORT_circuitocontable=&PARAMWEBREPORT_cuenta=&PARAMWEBREPORT_moneda=&PARAMWEBREPORT_Empresa='

urlComp = primera+Token+segunda

Consulta = requests.get(urlComp)

#print(urlComp)

if Consulta.status_code == 200:
    print("Ingreso ok")
else:
    print("No ingreso!")


df = json_normalize(Consulta.json())

df.to_excel('C:/Users/KPelaez.OMNI/Desktop/ComposicionClientes.xlsx')

    