import requests
import json
import pandas as pd
from pandas import json_normalize
from ValideToken import *
from datetime import *

Token = GeneradorToken('a843eb5642cbc99fed7af5d62fc1c764','176acd327ffd43fd858680d4a7efc475')

#Probamos traer la fecha en el formato predeterminado por finnegans. 
fecha_Hoy = datetime.today().strftime('%Y-%m-%d')

print(fecha_Hoy)

urlComp= f'https://api.teamplace.finneg.com/api/reports/COMPOSICIONSALDOSCLIENTES?ACCESS_TOKEN={Token}&PARAMWEBREPORT_fecha={fecha_Hoy}&PARAMWEBREPORT_organizacion=&PARAMWEBREPORT_circuitocontable=&PARAMWEBREPORT_cuenta=&PARAMWEBREPORT_moneda=&PARAMWEBREPORT_Empresa='

Consulta = requests.get(urlComp)


if Consulta.status_code == 200:
    print("Ingreso ok")
else:
    print("No ingreso!")
