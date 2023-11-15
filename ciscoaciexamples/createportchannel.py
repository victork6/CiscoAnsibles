#createPortchannel.py

#static_bind.py
#Importo todo de la libreria acitoolkit
from acitoolkit.acitoolkit import *
from inventory import *

#Defino lo que voy a pushear al tenant
tenant = Tenant('ACI-VICTOR-LABS')
#Creamos un App Profile dentro del tenant
app =AppProfile('AP_aciautoV', tenant)
#Creamos un VRF dentro del tenant previo
context = Context('VRF_victor-pruebas', tenant)
#Creamos el BridgeDomain 
bd = BridgeDomain('BD_Victor_pruebas', tenant)
#creamos el EPG
epg = EPG('EPG_ACIAUTO', app)
epg.add_bd(bd)
#Para asociar el Bridge Domain con exte EPG, le añadimos el contexto con 
bd.add_context(context)
#Iniciamos la subnet.
subnet = Subnet('subnet', bd)
#Ejemplo para añadir una subnet a este Bridge Domain
subnet.set_addr('6.6.1.1/24')
bd.add_subnet(subnet)
#Añadimos al EPG el Bridge Domain 
epg.add_bd(bd)


#Creación de EPG's Múltiple.
if1 = Interface('eth', '1', '101', '1', '39')
if2 = Interface('eth', '1', '101', '1', '39')

pc = PortChannel('pc1')
pc.attach(if1)
pc.attach(if2)

vlan_on_pc = L2Interface('vlan6_on_pc', 'vlan', '5')
vlan_on_pc.attach(pc)

vlan5_on_if1 = L2Interface('vlan5_on_if1', 'vlan', '1000')
vlan5_on_if1.attach(if1)

vlan5_on_if2 = L2Interface('vlan5_on_if2', 'vlan', '1000')
vlan5_on_if2.attach(if2)

epg.attach(vlan_on_pc)

description = 'acitoolkit tutorial aplication VV'
session = Session(APIC_URL, APIC_USERNAME, APIC_PASSWORD)
session.login()
resp = tenant.push_to_apic(session)

print ('Pushed the following Json to the APIC')
print ('URL:', tenant.get_url())
print ('JSON:', tenant.get_json())


