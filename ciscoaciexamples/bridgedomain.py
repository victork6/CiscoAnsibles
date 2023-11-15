# bridgedomain.py
#Importo todo de la libreria acitoolkit
from acitoolkit.acitoolkit import *

#Defino lo que voy a pushear al tenant
tenant = Tenant('ACI-VICTOR-LABS')
#Creamos un App Profile dentro del tenant
app =AppProfile('AP_aciautoV', tenant)
#Creamos un VRF dentro del tenant previo
context = Context('VRF_victor-pruebas', tenant)
#Creamos el BridgeDomain 
bd = BridgeDomain('BD_Victor_pruebas', tenant)
bd.add_context(context)
#snippets
description = 'acitoolkit tutorial aplication VV'
session = Session(APIC_URL, APIC_USERNAME, APIC_PASSWORD)
session.login()
resp = tenant.push_to_apic(session)

print ('Pushed the following Json to the APIC')
print ('URL:', tenant.get_url())
print ('JSON:', tenant.get_json())
