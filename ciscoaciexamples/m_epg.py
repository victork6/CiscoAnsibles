# epg_creation.py
#Importo todo de la libreria acitoolkit
from acitoolkit.acitoolkit import *

APIC_URL = "https://aiaaslab1.igrupobbva/"
APIC_PASSWORD = "C1sc0123"
APIC_USERNAME = "admin"
#Defino lo que voy a pushear al tenant
tenant = Tenant('ACI-VICTOR-LABS')
#Creamos un App Profile dentro del tenant
app =AppProfile('AP_aciautoV', tenant)
#Creamos un VRF dentro del tenant previo
context = Context('VRF_victor-pruebas', tenant)
#Creamos el BridgeDomain 
bd = BridgeDomain('BD_Victor_pruebas', tenant)
#Para asociar el Bridge Domain con exte EPG, le añadimos el contexto con 
bd.add_context(context)
#EPG
epg = EPG('epg_victor', app)
#Añadimos el epg y el bridgeDomain, es decir, lo unimos.
epg.add_bd(bd)

#snippets
description = 'acitoolkit tutorial aplication VV'
session = Session(APIC_URL, APIC_USERNAME, APIC_PASSWORD)
session.login()
resp = tenant.push_to_apic(session)

print ('Pushed the following Json to the APIC')
print ('URL:', tenant.get_url())
print ('JSON:', tenant.get_json())
