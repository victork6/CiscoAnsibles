from acitoolkit import Session

def obtener_info_epg(APIC_URL, APIC_USERNAME, APIC_PASSWORD, TENANT_NAME):
    conexion_exitosa = False  # Variable para rastrear el estado de la conexión
    try:
        session = Session(APIC_URL, APIC_USERNAME, APIC_PASSWORD)
        session.login()

        # Construir la consulta de API para obtener información de EPG
        query = f"/api/node/mo/uni/tn-{TENANT_NAME}/BD.json?query-target=subtree&target-subtree-class=fvRsPathAtt"

        epgs = session.get(query)

        # Crear una lista para almacenar la información de EPG
        epg_info = []

        # Procesar la información de EPG y agregarla a la lista
        for epg in epgs:
            print("estoy cogiendo información del EPG")
            epg_info.append({                
                "Nombre": epg.name,
                "Tenant": epg['fvRsPathAtt']['attributes']['tnDn'],
                "Bridge Domain": epg['fvRsPathAtt']['attributes']['dn'],
                "Encap VLAN": epg['fvRsPathAtt']['attributes']['encap'],
                "Tipo de Encap": epg['fvRsPathAtt']['attributes']['tDn']
            })

        session.logout()
        conexion_exitosa = True  # Se estableció la conexión con éxito
        print("Conexión exitosa")
        return epg_info
    except Exception as e:
        print("Error de conexión:", e)
        return []
    finally:
        if not conexion_exitosa:
            print("No conectado")
