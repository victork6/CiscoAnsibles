from netVictor.aci_utils import obtener_info_epg

def main():
    # Configura las credenciales y la URL de conexión a tu Cisco ACI
    APIC_URL = "https://sandboxapicdc.cisco.com"
    APIC_USERNAME = "admin"
    APIC_PASSWORD = "!v3G@!4@Y"
    TENANT_NAME = "Apha"
    print("No he entrado al while aun")

    while True:
        print("\n--- Menú ---")
        print("1: Obtener información de EPG")
        print("2: Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            epg_info = obtener_info_epg(APIC_URL, APIC_USERNAME, APIC_PASSWORD, TENANT_NAME)
            for epg in epg_info:
                print("EPG Nombre:", epg["Nombre"])
                print("  Tenant:", epg["Tenant"])
                print("  Bridge Domain:", epg["Bridge Domain"])
                print("  Encap VLAN:", epg["Encap VLAN"])
                print("  Tipo de Encap:", epg["Tipo de Encap"])
                print()
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "main":
    main()