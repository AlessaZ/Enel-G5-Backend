from connection import librenms_api

# Función para obtener información de los dispositivos
def get_links_by_device(dispositivo_id):
    response = librenms_api.get(f'/devices/{dispositivo_id}/links')
    if response.status_code == 200:
        links = response.json()
        return links['links']
    else:
        print(f'Error: {response.status_code}')
        return None

# Función para obtener información de los dispositivos
def get_vlans_by_device(dispositivo_id):
    response = librenms_api.get(f'/devices/{dispositivo_id}/vlans')
    if response.status_code == 200:
        vlans = response.json()
        return vlans['vlans']
    else:
        print(f'Error: {response.status_code}')
        return None