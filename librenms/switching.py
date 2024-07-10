import requests
from librenms.connection import librenms_api

# Función para obtener información de los dispositivos
def get_links_by_device(dispositivo_id):
    response = librenms_api.get(f'/devices/{dispositivo_id}/links')
    if isinstance(response, requests.Response):
        if response.status_code == 200:
            devices = response.json()
            return devices['links']
        else:
            print(f'Error: {response.status_code}')
            return None
    elif isinstance(response, dict):  # Handling if librenms_api.get() returns a dict
        return response.get('links', None)
    else:
        print('Unexpected response type')
        return None

# Función para obtener información de los dispositivos
def get_vlans_by_device(dispositivo_id):
    response = librenms_api.get(f'/devices/{dispositivo_id}/vlans')
    if isinstance(response, requests.Response):
        if response.status_code == 200:
            devices = response.json()
            return devices['vlans']
        else:
            print(f'Error: {response.status_code}')
            return None
    elif isinstance(response, dict):  # Handling if librenms_api.get() returns a dict
        return response.get('vlans', None)
    else:
        print('Unexpected response type')
        return None